/**
 * @file game.h
 * @author Jakub Delicat (delicat.kuba@gmail.com)
 * @brief It is class for ESP and Arduino
 * @version 0.1
 * @date 2021-11-13
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef GAME_H
#define GAME_H
#include <Arduino.h>

#include "player.h"
#include "throw.h"
#include "settings.h"

#ifndef MAX_PLAYERS
    #define MAX_PLAYERS 10
#endif

enum GameStatus{
    GameStatus_Active, GameStatus_Pause, GameStatus_Save, GameStatus_Finished
};
class Game{
    public:
    //TODO: wyebac id
        uint16_t id;
        Settings settings; 
        GameStatus status = GameStatus_Active;
        uint16_t throwingPlayerId;
        uint16_t round = 0;
        Player playerList[MAX_PLAYERS];
        uint8_t multiplier;
        uint8_t value;

        Game(const Settings &set);
        ~Game() {};
        StaticJsonDocument<SIZE_GAME_JSON> Document();
        GameStatus Loop();
        void Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc);
        virtual Throw ReadDartboard() = 0;
        virtual void SendDartboard() = 0;

};

#endif