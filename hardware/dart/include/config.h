#include <stdint.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7

#define MATRIX10x7


// array stored in flash memory
// rows coresponds to order of numbers on dashboard
// columns coresponds to multipliers of rings on dashboard

uint8_t pins_master[NUM_LINES_MASTER] = {2, 3, 4, 5, 11, 10, 9, 8, 7, 6};
uint8_t pins_slave[NUM_LINES_SLAVE] = {A7, 12, A4, A0, A3, A1, A2};