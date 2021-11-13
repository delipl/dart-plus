#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include <stdlib.h>

#include "game.h"
#include "ArduinoJson.h"


Dartboard dartboard(&pins_master, &pins_slave);
Player deli(1, "deli");
void setup() {
    Serial.begin(9600);
    uint16_t storage[MAX_PLAYERS];
    Vector<uint16_t> playerIds(storage);
    playerIds.push_back(1);
    playerIds.push_back(5);
    playerIds.push_back(15);
    playerIds.push_back(16);
    playerIds.push_back(13);

 
    

    Settings set(0, playerIds.size() , 301, false, false, playerIds);
    Serial.println("Creatiing settings...");
    Game game = Game(set);
    Serial.println("Loading game...");
    while(1);

    game.Loop();
}

void loop() {
    

    delay(2000);
}

