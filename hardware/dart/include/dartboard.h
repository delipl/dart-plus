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

// REMOVE THIS
#include "config.h"
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

#ifdef MATRIX_10x7 
const Throw SETUP_MATRIX[NUM_LINES_MASTER][NUM_LINES_SLAVE] = {
// 3x				         2x			        	1x		        		center
// 0            1           2           3           4           5           6
  {{3,1 },   	{3,  7}, 	{2,1 },	    {2,7 },	    {1,1},		{1,7 },		{2,25}  },
  {{3,18 },   	{3, 19},	{2,18},	    {2,19},	    {1,18},		{1,19},		{1,25}  },
  {{3,4 },	   	{3, 3 },	{2,4 },	    {2,3 },	    {1,4 },		{1,3 },		{0, 0}  },
  {{3,13 },   	{3, 17},	{2,13},	    {2,17},	    {1,13},		{1,17},		{0, 0}  },
  {{3,6 },	   	{3,  2},	{2,6},	    {2,2 },	    {1,6 },		{1,2 },		{0, 0}  },
  {{3,10 },   	{3,  15},	{2,10},	    {2,15},	    {1,10},		{1,15},		{0, 0}  },
  {{3,20 },	   	{3, 16},	{2,20},	    {2,16},	    {1,20},		{1,16},		{0, 0}  },
  {{3,5 },   	{3,  8},	{2,5 },	    {2, 8},	    {1,5},		{1,8 },		{0, 0}  },
  {{3,12 },	   	{3, 11},	{2,12},	    {2,11},	    {1,12},		{1,11},		{0, 0}  },
  {{3,9 },   	{3, 14},	{2,10},	    {2,14},	    {1,9},		{1,14},		{0, 0}  }
};
#else
const Throw SETUP_MATRIX[0][0];
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


    Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE]);


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