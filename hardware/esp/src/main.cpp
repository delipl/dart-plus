/*
 * WebSocketClientSocketIO.ino
 *
 *  Created on: 06.06.2016
 *
 */

#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <Hash.h>
#include <SocketIOclient.h>
#include <WebSocketsClient.h>
#include "server-client.h"
#include "settings.h"

void error_handler(const size_t &error_nr) {
}



std::shared_ptr<ServerClient> client;

void setup() {
    // USE_SERIAL.begin(921600);
    USE_SERIAL.begin(9600);

    // Serial.setDebugOutput(true);
    USE_SERIAL.setDebugOutput(true);

    USE_SERIAL.println();
    USE_SERIAL.println();
    USE_SERIAL.println();
    
    for (uint8_t t = 4; t > 0; t--) {
        USE_SERIAL.printf("[SETUP] BOOT WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(1000);
    }

    client = std::make_shared<ServerClient>("multimedia_plastek", "123454321", "192.168.0.7", 8000);
    delay(1000);
    // Settings set;
    // set.
    client->RequestSettings(1);
    USE_SERIAL.println();
    
    // if (not client->JoinGame(1)) {
    //     USE_SERIAL.println("[ERROR] Could not join to the room");
    //     error_handler(1);
    // }
}

void loop() {
    client->loop();
}
