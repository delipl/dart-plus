#ifndef SETTINGS_H
#define SETTINGS_H
#include "Arduino.h"
#include <stdint.h>
#include "config.h"
#include <ArduinoJson.h>

struct Settings{
    private:
    //TODO:
        uint16_t tab[1]; // -< do wyjebania
    public:
        uint16_t id;
        uint8_t numberOfPlayers;
        uint16_t startPoints;
        bool doubleIn;
        bool doubleOut;
        uint16_t playersId[MAX_PLAYERS];

        Settings();
        Settings(const uint16_t &id, const uint8_t &numberOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t *playersId);

        //TODO
        StaticJsonDocument<SIZE_SETTINGS_JSON> Document();
        void Deserialize(StaticJsonDocument<SIZE_SETTINGS_JSON> &doc);
};

#endif