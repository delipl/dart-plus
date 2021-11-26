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
    Serial.begin(115200);
    // dartboard.Init();

    // for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
    //     pinMode(pins_master[i], OUTPUT);
    //     digitalWrite(pins_master[i], HIGH);
    //     Serial.print("Ustawiam pina: ");
    //     Serial.println(pins_master[i]);
    // }   
    // for(uint8_t i = 0; i < NUM_LINES_SLAVE; ++i){
    //     if(pins_slave[i] != A7 && pins_slave[i] != A6) 
    //         pinMode(pins_slave[i], INPUT_PULLUP);
    // }
    // delay(100);
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

//     for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
//         digitalWrite(pins_master[i], HIGH);
//     }

//     for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
//         digitalWrite(pins_master[i], LOW);
//         for(uint8_t j = 0; j < NUM_LINES_SLAVE; ++j) {
//             // Pins A7 and A6 in Arduino Nano doesn't have GPIO Input Interface
//             if(pins_slave[j] == A7 || pins_slave[j] == A6){            
//                 if(analogRead(pins_slave[j] ) < 500 || analogRead(pins_slave[j] ) < 500){
                    
//                     Serial.print("Odczyt:\t");
//                     Serial.print(analogRead(pins_slave[j] ));
//                     Serial.print("\tpin:\t");
//                     Serial.print(pins_slave[j]);
//                     Serial.print("\tvalue:\t");
//                     Serial.println(SETUP_MATRIX[i][j].value*SETUP_MATRIX[i][j].multiplier);

                    
//                 }
//             }
//             else if(!digitalRead(pins_slave[j])){
//                 Serial.print("Odczyt:\t");
//                 Serial.print(digitalRead(pins_slave[j] ));
//                 Serial.print("\tpin:\t");
//                 Serial.print(pins_slave[j]);
//                 Serial.print("\tvalue:\t");
//                 Serial.println(SETUP_MATRIX[i][j].value*SETUP_MATRIX[i][j].multiplier);
//             }
            
//         }
        
//         digitalWrite(pins_master[i], HIGH);
//   }
//   delay(2000);
}