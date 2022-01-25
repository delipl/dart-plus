#ifndef CONFIG_H
#define CONFIG_H

#include <stdint.h>
#include <ArduinoJson.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7

#define MATRIX_10x7 true
#define MAX_PLAYERS 10
#define NICK_LENGTH 20 + 1
#define USE_SERIAL Serial
// TODO:
// MAKE SIZE OF DOCUMENTS



const size_t SIZE_THROW_JSON PROGMEM = JSON_OBJECT_SIZE(2);
const size_t SIZE_PLAYER_JSON PROGMEM = JSON_OBJECT_SIZE(3);
const size_t SIZE_SETTINGS_JSON PROGMEM = JSON_OBJECT_SIZE(6) + JSON_ARRAY_SIZE(MAX_PLAYERS) + 60;
#ifdef ARDUINO_CONFIG
const size_t SIZE_GAME_JSON PROGMEM =   JSON_OBJECT_SIZE(7) +  JSON_ARRAY_SIZE(MAX_PLAYERS) + 10 * JSON_OBJECT_SIZE(3) +
                                        61;
#endif

#ifdef ESP_CONFIG
const size_t SIZE_GAME_JSON PROGMEM =   JSON_OBJECT_SIZE(7) +  JSON_ARRAY_SIZE(MAX_PLAYERS) + 10 * JSON_OBJECT_SIZE(3) +
                                        61 + 19*MAX_PLAYERS;
#endif



// array stored in flash memory
// rows coresponds to order of numbers on dashboard
// columns coresponds to multipliers of rings on dashboard
    #ifdef ARDUINO_CONFIG
        const uint8_t pins_master[NUM_LINES_MASTER]  = {2,3,4,5,6,7,8,9,10,11};
        const uint8_t pins_slave[NUM_LINES_SLAVE]  = {12, A7, A0, A6, A1, A3, A2};
    #endif


    //todo: compilation for every this_board_id
    constexpr uint8_t this_board_id = 0x0001;
#endif