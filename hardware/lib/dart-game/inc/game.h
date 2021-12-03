/**
 * @file game.h
 * @author Jakub Delicat (delicat.kuba@gmail.com)
 * @brief 
 * @version 0.1
 * @date 2021-11-13
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef GAME_H
#define GAME_H

#include "player.h"
#include "Arduino.h"
#include "settings.h"
#ifndef MAX_PLAYERS
    #define MAX_PLAYERS 10
#endif

enum GameStatus{
    GameStatus_Active, GameStatus_Pause, GameStatus_Save, GameStatus_Finished
};



class Game{
    private:
        // String json;
    public:
    //TODO: wyebac id
        uint16_t id;
        Settings settings; 
        GameStatus status = GameStatus_Active;
        uint16_t throwingPlayerId;
        uint16_t round = 0;
        Player playerList[MAX_PLAYERS];
        Throw lastThrow;

        Game(const Settings &set);
        ~Game(); // do wyjebania

        StaticJsonDocument<SIZE_GAME_JSON> Document();
        void Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc);

        GameStatus Loop();
};

#endif