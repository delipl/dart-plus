
#ifndef GAMEAPI_H
#define GAMEAPI_H

#include <Arduino.h>
#include <SoftwareSerial.h>
#include "game.h"
#include "dartboard.h"



extern SoftwareSerial EspSerial;
extern Throw ReadDartboard();
extern void SendToServer();

class GameApi : public Game {
   public:
    GameApi(const Settings &set) : Game(set) {
        Serial.println("Stworzono gre");
    };
    GameStatus Loop();
};

#endif