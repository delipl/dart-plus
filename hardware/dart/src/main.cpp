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
    Serial.begin(9600);
    Serial.println("\nInitiating dartboard...");
    dartboard.Init();


    uint16_t storage[MAX_PLAYERS];
    Vector<uint16_t> playerIds(storage);
    playerIds.push_back(1);
    playerIds.push_back(5);
    playerIds.push_back(15);
    playerIds.push_back(16);
    playerIds.push_back(13);

    StaticJsonDocument<SIZE_PLAYER_JSON> doc;
    Player deli;
    
    doc["id"] = 0x5987;
    doc["nick"] = "deli";
    doc["points"] = 555;
    doc["attemps"] = 59;
    deli.Deserialize(doc);
    Serial.println(deli.Serialize());

    while(1);

    // TODO
    // doc["lastThrow"] = Throw(2, 20);
    // doc

    // Throw lol;
    // StaticJsonDocument<16> doc;
    // doc["multiplier"] = 13;
    // doc["value"] = 16;
    // lol.Deserialize(doc);
    // serializeJson(doc, lol);
    // // serializeJson(doc, Serial);
    // Serial.print("LOL: ");
    // Serial.println(lol.Serialize());

    

    // Serial.println(dupa.Serialize());
    // dupa.Deserialize(doc);
    // Serial.println(dupa.Serialize());
    
    // while(1);
    // Settings set(0, playerIds.size() , 301, false, false, playerIds);
    // Serial.println("Creatiing settings...");
    // Game game(set);
    // Serial.println("Loading game...");
    
    // game.Loop();
    // Serial.println("After LOOP");
}

void loop() {
    
    // Throw hit(0,0);
    // hit = dartboard.ReadThrow();
    // if(hit != Throw(0,0)){
    //     Serial.println("" + hit);
    // }
    // delay(100);
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

