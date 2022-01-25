#ifndef SERVERCLIENT_H
#define SERVERCLIENT_H

#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <Hash.h>
#include <SocketIOclient.h>
#include <WebSocketsClient.h>

#include "config.h"
enum RequestError {
    RequestError_OK,
    RequestError_Error
};


class ServerClient{
    private:
        const String stassid;
        const String stapsk;
        const String server_ip;
        const uint16_t server_port;
        const String url;

        ESP8266WiFiMulti WiFiMulti;
        inline static SocketIOclient socketIO;

        StaticJsonDocument<SIZE_GAME_JSON> ReadGame(uint8_t *payload);
        StaticJsonDocument<SIZE_SETTINGS_JSON> ReadSettings(uint8_t *payload);

       public:
        inline static socketIOmessageType_t status;
        inline static bool connection_initialied = false;
        static void event_callback(socketIOmessageType_t type, uint8_t *payload, size_t length);
        uint16_t game_id = 0;
        ServerClient(const String &stassid, const String &stapsk, const String &server_ip, const uint16 server_port, const String &url = "/socket.io/?EIO=4");
        String RequestSettings(const uint8_t &board_id);
        bool JoinGame(const uint8_t &game_id);

        RequestError SendGame(StaticJsonDocument<SIZE_GAME_JSON> doc);

        void loop();
};

#endif