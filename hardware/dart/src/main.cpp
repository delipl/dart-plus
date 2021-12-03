#include <Arduino.h>
#include <stdint.h>
#include <ArduinoJson.h>
#include <stdlib.h>

#include "config.h"
#include "dartboard.h"
Dartboard dartboard(&pins_master, &pins_slave);


#include "player.h"
#include "game.h"

void setup() {
    // Serial.begin(115200);
}

void loop() {  

    Serial.begin(115200);
    Serial.println("\nInitiating dartboard...");
    delay(100);
    dartboard.Init();
    delay(100);

    uint16_t playerIds[MAX_PLAYERS];
    for(int i = 0; i < MAX_PLAYERS; ++i){
        playerIds[i] = i;
    }
    Serial.println("Creatiing settings...");
    Settings set(0, MAX_PLAYERS , UINT16_MAX, false, false, playerIds);   
    Game game(set);
    game.Loop();
}