#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include <stdlib.h>

#include "ArduinoJson.h"
#include "dartboard.h"
Dartboard dartboard(&pins_master, &pins_slave);
#include "player.h"
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
    
    Throw hit(0,0);
    hit = dartboard.ReadThrow();
    if(hit != Throw(0,0)){
        Serial.println("" + hit);
    }
    delay(100);
    //  for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
    //     digitalWrite((pins_master)[i], HIGH);
    //  }
    //  digitalWrite((pins_master)[0], LOW);
    //     if((pins_slave)[1] == A7){
    //             Serial.print("TAB: ");
    //  Serial.println((pins_master)[0]);
    // Serial.print("Analog7 : ");
    //  Serial.println(analogRead(A7));
    //  Serial.print("Analog6 : ");
    //  Serial.println(analogRead(A6));
        // }
     
}

