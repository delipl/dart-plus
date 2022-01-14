#ifndef SERVERCLIENT_H
#define SERVERCLIENT_H

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#include "config.h"
enum RequestError{
    RequestError_OK, RequestError_Error
};

class ServerClient{
    private:
        const String stassid;
        const String stapsk;
        const String ipAddress;

    public:
        ServerClient(const String &stassid, const String &stapsk, const String &ipAddress );

        RequestError SendSettings(StaticJsonDocument<SIZE_SETTINGS_JSON> doc);
        RequestError SendGame(StaticJsonDocument<SIZE_GAME_JSON> doc);
            
        
};

#endif