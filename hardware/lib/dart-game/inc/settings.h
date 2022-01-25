#ifndef SETTINGS_H
#define SETTINGS_H
#include <ArduinoJson.h>
#include <stdint.h>

#include <initializer_list>
#include <utility>
#include <vector>
#include <memory>

#include "Arduino.h"
#include "player.h"
struct Settings{
    public:
        const uint16_t id;
        const uint16_t startPoints;
        const bool doubleIn;
        const bool doubleOut;
        std::vector<std::shared_ptr<Player>> players;
        Settings(const uint16_t &id, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, const std::initializer_list<std::shared_ptr<Player>> &list);

        // StaticJsonDocument<SIZE_SETTINGS_JSON> Document();
        // void Deserialize(StaticJsonDocument<SIZE_SETTINGS_JSON> &doc);
};

#endif