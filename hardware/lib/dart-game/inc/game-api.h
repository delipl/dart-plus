
#ifndef GAMEAPI_H
#define GAMEAPI_H

#include <Arduino.h>
#include "game.h"
#include "dartboard.h"
#include "server-client.h"

class GameApi : public Game {
   public:
    explicit GameApi(const Settings &set) : Game(set) {
        Serial.println("Stworzono gre");
    };
    ~GameApi(){};
    virtual Throw ReadDartboard();
	virtual void SendDartboard();
    
};

#endif