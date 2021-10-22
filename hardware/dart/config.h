#include <stdint.h>

#define NUM_LINES_MASTER        10
#define NUM_LINES_SLAVE         7
#define GET_LOOKUP_VALUE(i, j)  pgm_read_byte_near(&matrix_lookup[(i)][(j)])

// array stored in flash memory
const int8_t matrix_lookup[NUM_LINES_MASTER][NUM_LINES_SLAVE] PROGMEM = {
// 3x       2x      3x      2x      1x  	center  1x
  {3*9,		2*9,	3*14,	2*14,	14,		2*25,	9},
  {3*12,	2*12,	3*11,	2*11,	11,		25,		12},
  {3*5,		2*5,	3*8,	2*8,	8,		-1,		5},
  {3*20,	2*20,	3*16,	2*16,	16,		-1,		20},
  {3*10,	2*10,	3*15,	2*15,	15,		-1,		10},
  {3*6,		2*6,	3*2,	2*2,	2,		-1,		6},
  {3*13,	2*13,	3*17,	2*17,	17,		-1,		13},
  {3*4,		2*4,	3*3,	2*3,	3,		-1,		4},
  {3*18,	2*18,	3*19,	2*19,	19,		-1,		18},
  {3*1,		2*1,	2*7,	2*7,	7,		-1,		1}
};
