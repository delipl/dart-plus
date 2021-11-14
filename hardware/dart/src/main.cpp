#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include <stdlib.h>

#include "ArduinoJson.h"

#include "dartboard.h"
Dartboard dartboard(&pins_master, &pins_slave) PROGMEM;


#include "player.h"
#include "game.h"

void setup() {
    Serial.begin(115200);
    Serial.println("\nInitiating dartboard...");
    delay(100);
    dartboard.Init();


    uint16_t playerIds[MAX_PLAYERS];
    // Vector<uint16_t> playerIds(storage);

    // for(int i = 0; i < MAX_PLAYERS; ++i){
    //     playerIds.push_back(i);
    // }
    Settings set(0, MAX_PLAYERS , UINT16_MAX, false, false, playerIds);

    // Serial.println(set.amountOfPlayers);
    Serial.println("Creatiing settings...");
    Game game(set);
    Serial.println("Test Serialization");
    serializeJsonPretty(game.Document(), Serial);

    Serial.println("Loading game...");
    for(int i = 0; i < game.settings.amountOfPlayers; ++i){

        Serial.print(game.playerList[i].nick);
        Serial.println(" joined the game.");

    }
    while(1);
    
    game.Loop();
    Serial.println("After LOOP");
}

void loop() {  
}