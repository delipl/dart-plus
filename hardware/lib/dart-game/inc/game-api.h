
#ifndef GAMEAPI_H
#define GAMEAPI_H

#include <Arduino.h>
#include <SoftwareSerial.h>
#include "game.h"
#include "dartboard.h"

extern SoftwareSerial mySerial;
extern Dartboard dartboard;
class GameApi : public Game{
    public:   
        GameApi(const Settings &set): Game(set){
            Serial.println("Stworzono gre");
        };
        GameStatus Tick();
};

#endif