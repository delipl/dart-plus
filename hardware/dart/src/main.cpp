#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include <stdlib.h>

#include "game.h"
#include "ArduinoJson.h"


Dartboard dartboard(&pins_master, &pins_slave);
Player deli(1, "deli");
void setup() {
    Serial.begin(9600);
    uint16_t playerIds[] = {11, 2, 3, 5, 4};
    Settings set(0, 5, 301, false, false, playerIds);

    Game *game = new Game(set);

    game->Loop();
}

void loop() {
    

    delay(2000);
}

