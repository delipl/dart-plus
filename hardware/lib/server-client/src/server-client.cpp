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

RequestError ServerClient::SendGame(StaticJsonDocument<SIZE_GAME_JSON> doc) {
    JsonArray array = doc.to<JsonArray>();

    // add evnet name
    // Hint: socket.on('event_name', ....
    array.add("game_loop");

    // add payload (parameters) for the event
    String doc_raw;
    serializeJson(doc, doc_raw);
    String out = "{ \"game_loop\" :[" + doc_raw +"]}";
    // JSON to String (serializion)
    // socketIO.sendEVENT(out);
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

template <typename second>
String make_event(String event, std::vector<std::pair<String, second>> list) {
    // creat JSON message for Socket.IO (event)
    DynamicJsonDocument doc(1024);
    JsonArray array = doc.to<JsonArray>();

    // add evnet name
    // Hint: socket.on('event_name', ....
    array.add(event);

    // add payload (parameters) for the event
    JsonObject param1 = array.createNestedObject();
    for (const auto &elem : list) {
        param1[elem.first] = elem.second;
    }

    // JSON to String (serializion)
    String output;
    serializeJson(doc, output);
    return output;
}

void ServerClient::loop(){
    socketIO.loop();
    // if(not connection_initialied and status == sIOtype_CONNECT){
    //     connection_initialied = true;
    //     String out = make_event<int>("begin", {{"game_id", game_id}});
    //     // socketIO.sendEVENT(out);
    // }
}