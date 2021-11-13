#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include <stdlib.h>

#include "ArduinoJson.h"
#include "dartboard.h"
Dartboard dartboard(&pins_master, &pins_slave);
#include "game.h"



Player deli(1, "deli");
void setup() {
    Serial.begin(9600);
    Serial.println("\nInitiating dartboard...");
    dartboard.Init();


    // uint16_t storage[MAX_PLAYERS];
    // Vector<uint16_t> playerIds(storage);
    // playerIds.push_back(1);
    // playerIds.push_back(5);
    // playerIds.push_back(15);
    // playerIds.push_back(16);
    // playerIds.push_back(13);

 
    

    // Settings set(0, playerIds.size() , 301, false, false, playerIds);
    // Serial.println("Creatiing settings...");
    // Game game(set);
    // Serial.println("Loading game...");
    
    // game.Loop();
    // Serial.println("After LOOP");
    // game.playerList[0].Throwing();
    // Serial.println(String("\t") + game.playerList[0].lastThrow);
}

void loop() {
    Serial.println("\t" + dartboard.ReadThrow());
    delay(500);
}

