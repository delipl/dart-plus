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

#include <memory>

#include "player.h"
#include "settings.h"
#include "throw.h"

#ifndef MAX_PLAYERS
#define MAX_PLAYERS 10
#endif

enum GameStatus {
    GameStatus_Active,
    GameStatus_Pause,
    GameStatus_Save,
    GameStatus_Finished
};

class Game {
   public:
    const uint16_t id;
    Settings settings;
    GameStatus status = GameStatus_Active;
    uint16_t throwingPlayerId;
    uint16_t round = 0;
    uint8_t multiplier;
    uint8_t value;

    Game(const Settings &set);
    ~Game(){};
    StaticJsonDocument<SIZE_GAME_JSON> Document() const;
    void loop();
    bool Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc);

    virtual Throw ReadDartboard() const = 0;
    virtual void SendDartboard() const = 0;
    virtual void RequestGameLoop() = 0;
};

#endif