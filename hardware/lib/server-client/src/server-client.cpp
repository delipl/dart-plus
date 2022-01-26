#include "server-client.h"

ServerClient::ServerClient(const String &stassid, const String &stapsk, const String &server_ip, const uint16 server_port, const String &url) : 
stassid{stassid}, stapsk{stapsk}, server_ip{server_ip}, server_port{server_port}, url{url} {
    // disable AP
    if (WiFi.getMode() & WIFI_AP) {
        WiFi.softAPdisconnect(true);
    }

    WiFiMulti.addAP(stassid.c_str(), stapsk.c_str());

    // WiFi.disconnect();
    while (WiFiMulti.run() != WL_CONNECTED) {
        delay(100);
    }

    String ip = WiFi.localIP().toString();
    USE_SERIAL.printf("[SETUP] WiFi Connected %s\n", ip.c_str());;
    USE_SERIAL.printf("[WEBSOCKETIO] Host ip: %s", server_ip.c_str());

    socketIO.begin(server_ip, server_port, "/socket.io/?EIO=4");
    socketIO.onEvent(event_callback);
}

String ServerClient::RequestSettings(const uint8_t &board_id) {
    if ((WiFi.status() == WL_CONNECTED)) {
        WiFiClient client;
        HTTPClient http;
        String request_ip = String("http://") +  server_ip + ":" + String(server_port) + String("/dartBoard/settings");
        http.begin(client, request_ip);
        USE_SERIAL.printf("[HTTP] Request ip: %s\n", request_ip.c_str());

        http.addHeader("Content-Type", "application/json");

        USE_SERIAL.print("[HTTP] POST...\n");
        String json = "{\"board_id\":" + String(board_id) + "}";
        USE_SERIAL.printf("[HTTP] Message: %s\n",json.c_str());
        int httpCode = http.POST(json);

        if (httpCode > 0) {
            USE_SERIAL.printf("[HTTP] POST... code: %d\n", httpCode);

            if (httpCode == HTTP_CODE_OK) {
                const String &payload = http.getString();
                USE_SERIAL.println("received payload:\n<<");
                USE_SERIAL.println(payload);
                USE_SERIAL.println(">>");
                return payload;
            }
        } else {
            USE_SERIAL.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }
    }
    return String();
}

bool ServerClient::JoinGame(const uint8_t &game_id){
    USE_SERIAL.print("[WEBSOCKETIO] Joining to the game room...");
    

    int tries = 0;
    while (status != sIOtype_CONNECT) {
        USE_SERIAL.print(".");
        ++tries;
        delay(500);
        if (tries == 20) return false;
    }

    return true;
}

void ServerClient::send_event(const String &event_name, const String &json, const String &name_space) {
    String out = name_space + ",[\"" + event_name + "\"," + json + "]";
    USE_SERIAL.printf("[WEBSOCKETIO] Sending: \n>>>==============\n%s\n==============<<<\n", out.c_str());
    socketIO.sendEVENT(out);
}

RequestError ServerClient::SendGame(const String &doc) {
    send_event("game_loop", doc, "/esp");
    return RequestError_OK;
}

void ServerClient::event_callback(socketIOmessageType_t type, uint8_t *payload, size_t length) {
    status = type;
    switch (type) {
        case sIOtype_DISCONNECT:
            USE_SERIAL.printf("[IOc] Disconnected!\n");
            connection_initialied = false;
            break;
        case sIOtype_CONNECT:
            USE_SERIAL.printf("[IOc] Connected to url: %s\n", payload);

            // join default namespace (no auto join in Socket.IO V3)
            socketIO.send(sIOtype_CONNECT, "/esp");
            // USE_SERIAL.printf("[WEBSOCKETIO] First connection message: %s.\n", out.c_str());
            break;
        case sIOtype_EVENT:
            USE_SERIAL.printf("[IOc] get event: %s\n", payload);
            //todo: if gevent is "game_loop"
            break;
        case sIOtype_ACK:
            USE_SERIAL.printf("[IOc] get ack: %u\n", length);
            hexdump(payload, length);
            break;
        case sIOtype_ERROR:
            USE_SERIAL.printf("[IOc] get error: %u\n", length);
            hexdump(payload, length);
            break;
        case sIOtype_BINARY_EVENT:
            USE_SERIAL.printf("[IOc] get binary: %u\n", length);
            hexdump(payload, length);
            break;
        case sIOtype_BINARY_ACK:
            USE_SERIAL.printf("[IOc] get binary ack: %u\n", length);
            hexdump(payload, length);
            break;
    }
}

void ServerClient::loop(){
    socketIO.loop();
    if(not connection_initialied and status == sIOtype_CONNECT){
        connection_initialied = true;
        send_event("join_room", "{\"game_id\":" + String(game_id) + "}", "/esp");
    }
}