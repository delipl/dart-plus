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
        const uint16_t id;
        const uint16_t board_id;
        const std::string nick;
        uint8_t attempts = 0;
        uint16_t points;

        Player();
        Player(const uint16_t &id, const uint16_t &board_id, const std::string &nick, const uint16_t &points = 301);
        Player (const Player &other);
        Player &operator=(const Player &other);
        bool is_same(const Player &player) const;
};

#endif