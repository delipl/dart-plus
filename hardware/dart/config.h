#include <stdint.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7
#define GET_LOOKUP_VALUE(i, j)  pgm_read_byte_near(&matrix_lookup[(i)][(j)])

// array stored in flash memory
// rows coresponds to order of numbers on dashboard
// columns coresponds to multipliers of rings on dashboard
const int8_t matrix_lookup[NUM_LINES_MASTER][NUM_LINES_SLAVE] PROGMEM = {
// 3x				2x				1x				center
  {3*14,	3*9,	2*14,	2*9,	14,		9,		2*25},
  {3*11,	3*12,	2*11,	2*12,	11,		12,		25},
  {3*8,		3*5,	2*8,	2*5,	8,		5,		-1},
  {3*16,	3*20,	2*16,	2*20,	16,		20,		-1},
  {3*7,		3*1,	2*7,	2*1,	7,		1,		-1},
  {3*19,	3*18,	2*19,	2*18,	19,		18,		-1},
  {3*3,		3*4,	2*3,	2*4,	3,		4,		-1},
  {3*17,	3*13,	2*17,	2*13,	17,		13,		-1},
  {3*2,		3*6,	2*2,	2*6,	2,		6,		-1},
  {3*15,	3*10,	2*15,	2*10,	15,		10,		-1}
};
