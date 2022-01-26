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
#include "game-api.h"
#include "server-client.h"
void error_handler(const size_t &error_nr) {
}

std::shared_ptr<ServerClient> client;
std::shared_ptr<GameApi> game;


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
}
bool first = true;
void loop() {
    if (first) {
        first = false;
        client = std::make_shared<ServerClient>("multimedia_plastek", "123454321", "192.168.0.21", 8000);
        USE_SERIAL.print("[HTTP] Requesting setting...");
        auto raw_settings = client->RequestSettings(this_board_id);
        while (raw_settings == String()) {
            USE_SERIAL.print(".");
            raw_settings = client->RequestSettings(this_board_id);
            delay(500);
        }
        StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
        deserializeJson(doc, raw_settings);
        Settings set(doc);

        USE_SERIAL.println("==============================================");

        game = std::make_shared<GameApi>(set);
        client->game_id = game->id;
        USE_SERIAL.println();
        USE_SERIAL.println("[GAME] Game Initialized");
    }
    
    while (game->status != GameStatus_Finished) {
        if (not client->JoinedGame()) return;
        client->loop();
        game->loop();
      
    }
    // first = true;
}
