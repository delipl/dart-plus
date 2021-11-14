#ifndef SETTINGS_H
#define SETTINGS_H
#include "Arduino.h"
#include <stdint.h>
#include "config.h"

struct Settings{
    private:
    //TODO:
        uint16_t tab[1]; // -< do wyjebania
    public:
        const uint16_t id;
        uint8_t amountOfPlayers;
        const uint16_t startPoints;
        const bool doubleIn;
        const bool doubleOut;
        uint16_t playersId[MAX_PLAYERS];

        Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t *playersId);

        //TODO
        void Deserialization();
};

#endif