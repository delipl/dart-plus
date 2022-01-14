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
#include <string.h>
#include "config.h"


class Player{
    public:
        uint16_t id;
        char nick[NICK_LENGTH];
        uint16_t points;
        uint8_t attempts = 0;

        Player();
        Player(const uint16_t &id, const char nick[NICK_LENGTH], const uint16_t &points = 301, const uint8_t &attempts = 0);
        Player &operator=(const Player &other);

        StaticJsonDocument<SIZE_PLAYER_JSON> Document();

        void Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc);

        
};

#endif