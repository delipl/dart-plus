/**
 * @file player.h
 * @author Jakub Delicat (delicat.kuba@gmail.com)
 * @brief 
 * @version 0.1
 * @date 2021-11-12
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef PLAYRER_H
#define PLAYRER_H

#include <Arduino.h>
#include <ArduinoJson.h>
#include <dartboard.h>
#include <string.h>

/**
 * @brief OK - good throw just subtract, END - finish game player has 0 points, ERROR - player throw to much
 */
enum ThrowStatus {
    ThrowStatus_OK, ThrowStatus_END, ThrowStatus_ERROR  
};

extern Dartboard dartboard;

class Player{
    public:
        uint16_t id;
        char nick[NICK_LENGTH];
        uint16_t points;
        uint8_t attemps = 0;

        Player();
        Player(const uint16_t &id, const char nick[NICK_LENGTH], const uint16_t &points = 301, const uint8_t &attemps = 0);
        Player &operator=(const Player &other);
        // TODO: substraing points in game
        const ThrowStatus Throwing();
        StaticJsonDocument<SIZE_PLAYER_JSON> Document();

        void Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc);

        
};

#endif