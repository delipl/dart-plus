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
        String nick;
        uint16_t points;
        uint8_t attemps = 0;
        Throw lastThrow = Throw(0,0);

        Player();
        Player(const uint16_t &id, const String &nick, const uint16_t &points = 301, const uint8_t &attemps = 0);
        Player &operator=(const Player &other);


        const ThrowStatus Throwing();
};

String operator+(const String &prefix, const Player &player);

#endif