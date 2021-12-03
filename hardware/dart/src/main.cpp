#include <Arduino.h>
#include <stdint.h>
#include <ArduinoJson.h>
#include <SoftwareSerial.h>
#include <stdlib.h>
#include "config.h"
#include "dartboard.h"
Dartboard dartboard(&pins_master, &pins_slave);


#include "player.h"
#include "game-api.h"



void setup() {
    // Serial.begin(115200);
}
SoftwareSerial mySerial(A5, A4); // RX, TX
void loop() {  

    Serial.begin(9600);
    mySerial.begin(9600);
    Serial.println("\nInitiating dartboard...");
    delay(100);
    dartboard.Init();
    delay(100);

    uint16_t playerIds[MAX_PLAYERS];
    for(int i = 0; i < MAX_PLAYERS; ++i){
        playerIds[i] = i;
    }
    Serial.println("Loading settings...");
    Settings set(0, MAX_PLAYERS , UINT16_MAX, false, false, playerIds);   
    Serial.println("Loading game...");
    GameApi game(set);
    Serial.println("Loaded game...");
    // Send settings
    serializeJson(game.settings.Document(), mySerial);
    
    delay(100);
    Serial.println("\nWelcome to Dart-Plus");

    while(true){
        game.Tick();
    }
}