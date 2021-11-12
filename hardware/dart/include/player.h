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
#include <dartboard.h>

class Player{
    public:
        Dartboard  *dartboard;
        uint32_t id;
        const String name;
        const String nick;
        uint8_t points;
        uint8_t attemps = 3;

        Player(Dartboard * dartboard,const uint32_t &id, const String &name, const String &nick, const uint8_t &points = 301, const uint8_t &attemps = 3);

        const Throw Throw();
};

#endif