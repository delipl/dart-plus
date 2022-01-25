
#ifndef GAMEAPI_H
#define GAMEAPI_H

#include <Arduino.h>

#include "dartboard.h"
#include "game.h"
#include "server-client.h"

extern std::shared_ptr<ServerClient> client;
class GameApi : public Game {
   public:
    
    GameApi(const Settings &set) : Game(set) {
        Serial.println("Stworzono gre");
    };
    ~GameApi(){};
    Throw ReadDartboard() const;
    void SendDartboard() const;
    void RequestGameLoop();
};

#endif