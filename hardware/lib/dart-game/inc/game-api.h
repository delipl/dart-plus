
#ifndef GAMEAPI_H
#define GAMEAPI_H

#include <Arduino.h>

#include "dartboard.h"
#include "game.h"
#include "server-client.h"

class GameApi : public Game {
   public:
    GameApi(const Settings &set) : Game(set) {
        Serial.println("Stworzono gre");
    };
    ~GameApi(){};
    virtual Throw ReadDartboard() const;
    virtual void SendDartboard() const;
    virtual void RequestGameLoop();
};

#endif