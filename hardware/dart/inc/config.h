#ifndef CONFIG_H
#define CONFIG_H

#include <stdint.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7

#define MATRIX_10x7 true
#define MAX_PLAYERS 20

// array stored in flash memory
// rows coresponds to order of numbers on dashboard
// columns coresponds to multipliers of rings on dashboard
const uint8_t pins_master[NUM_LINES_MASTER] = {2,3,4,5,6,7,8,9,10,11};
const uint8_t pins_slave[NUM_LINES_SLAVE] = {12, A7, A0, 13, A1, A3, A2};
// const uint8_t pins_master[NUM_LINES_MASTER] = { 50, 50, 50, 50, 60, 70, 80, 90, 90,110};
// const uint8_t pins_slave[NUM_LINES_SLAVE] = {120, 50, 50, 50, 50, 50, 50};
#endif