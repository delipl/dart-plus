#ifndef CONFIG_H
#define CONFIG_H

#include <stdint.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7

#define MATRIX_10x7 true
#define MAX_PLAYERS 10
#define NICK_LENGTH 20 + 1

// TODO:
// MAKE SIZE OF DOCUMENTS

#define SIZE_THROW_JSON 16
#define SIZE_PLAYER_JSON 53
#define SIZE_SETTINGS_JSON 1024
#define SIZE_GAME_JSON 500

// array stored in flash memory
// rows coresponds to order of numbers on dashboard
// columns coresponds to multipliers of rings on dashboard
const uint8_t pins_master[NUM_LINES_MASTER] PROGMEM = {2,3,4,5,6,7,8,9,10,11};
const uint8_t pins_slave[NUM_LINES_SLAVE] PROGMEM = {12, A7, A0, A6, A1, A3, A2};
#endif