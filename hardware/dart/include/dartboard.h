/**
 * @file dartboard.h
 * @author Jakub Delicat (delicat.kuba@gmail.com)
 * @brief Dartboard class manages dartboard and return points
 * @version 0.1
 * @date 2021-11-11
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef DARTBOARD_H
#define DARTBOARD_H

#include "Arduino.h"
#include <stdint.h>

#ifndef NUM_LINES_MASTER
    #define NUM_LINES_MASTER  10
    #define NUM_LINES_SLAVE  7
#endif

/**
 * @brief Throw struct describes hit place on dartboard
 * 
 */
struct Throw{
    const uint8_t multiplier;
    const uint8_t value;
    

    Throw(const uint8_t &multiplier, const uint8_t &value);
};

#ifdef MATRIX10x7
const Throw matrix_lookup[NUM_LINES_MASTER][NUM_LINES_SLAVE] = {
// 3x				2x				1x				center
  {{3,14},   	{3, 9 }, 	{2,14},	    {2,9 },	    {1,14},		{1,9 },		{2,25}  },
  {{3,11},   	{3, 12},	{2,11},	    {2,12},	    {1,11},		{1,12},		{1,25}  },
  {{3,8 },	   	{3, 5 },	{2,8 },	    {2,5 },	    {1,8 },		{1,5 },		{0, 0}  },
  {{3,16},   	{3, 20},	{2,16},	    {2,20},	    {1,16},		{1,20},		{0, 0}  },
  {{3,7 },	   	{3, 1 },	{2,7 },	    {2,1 },	    {1,7 },		{1,1 },		{0, 0}  },
  {{3,19},   	{3, 18},	{2,19},	    {2,18},	    {1,19},		{1,18},		{0, 0}  },
  {{3,3 },	   	{3, 4 },	{2,3 },	    {2,4 },	    {1,3 },		{1,4 },		{0, 0}  },
  {{3,17},   	{3, 13},	{2,17},	    {2,13},	    {1,17},		{1,13},		{0, 0}  },
  {{3,2 },	   	{3, 6 },	{2,2 },	    {2,6 },	    {1,2 },		{1,6 },		{0, 0}  },
  {{3,15},   	{3, 10},	{2,15},	    {2,10},	    {1,15},		{1,10},		{0, 0}  }
};
#endif



/**
 * @brief Describes points matrix and reads dartboard
 */
class Dartboard{
public:
    /**
     * @brief Matrix with points place definition
     */
    const Throw (*matrix_lookup)[NUM_LINES_MASTER][NUM_LINES_SLAVE];

    const uint8_t (*pins_master)[NUM_LINES_MASTER];
    const uint8_t (*pins_slave)[NUM_LINES_SLAVE];


    Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE], const Throw (*matrix)[NUM_LINES_MASTER][NUM_LINES_SLAVE]);


    /**
     * @brief Read hit dartboard
     * @return Throw hit place
     */
    Throw ReadThrow();

    /**
     * @brief Set pinModes
     */
    void Init();
};

#endif