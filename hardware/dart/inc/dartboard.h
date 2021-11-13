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
#include <stdint.h>

#include "Arduino.h"
#include "ArduinoJson.h"
// REMOVE THIS
#include "config.h"
#define JSON_LENGHT

/**
 * @brief 
 * 
 */
class Throw{
    public:
    uint8_t multiplier;
    uint8_t value;

    Throw &operator=(const Throw &other);
    bool operator==(const Throw &other) const;
    bool operator!=(const Throw &other) const;
    bool operator!() const;
    bool operator==(const int &other) const;
    bool operator>(const int &other) const;
    bool operator<(const int &other) const;

    Throw(const uint8_t &multiplier, const uint8_t &value);
    Throw(){};
};
uint16_t operator- (const uint16_t &points, const Throw &hit);
uint16_t operator+ (const uint16_t &points, const Throw &hit);



#ifndef NUM_LINES_MASTER
    #define NUM_LINES_MASTER  10
    #define NUM_LINES_SLAVE  7
#endif

#ifdef MATRIX_10x7 
// it is possioble to add 6 buttons on 6 collumn
const Throw SETUP_MATRIX[NUM_LINES_MASTER][NUM_LINES_SLAVE]  ={
// 3x				         2x			        	1x		        		center
// 0            1           2           3           4           5           6
  {{3,1 },   	{3,  7}, 	{2,1 },	    {2,7 },	    {1,1},		{1,7 },		{1, 255}  },
  {{3,18 },   	{3, 19},	{2,18},	    {2,19},	    {1,18},		{1,19},		{1, 255}  },
  {{3,4 },	   	{3, 3 },	{2,4 },	    {2,3 },	    {1,4 },		{1,3 },		{1, 255}  },
  {{3,13 },   	{3, 17},	{2,13},	    {2,17},	    {1,13},		{1,17},		{1, 255}  },
  {{3,6 },	   	{3,  2},	{2,6},	    {2,2 },	    {1,6 },		{1,2 },		{1, 255}  },
  {{3,10 },   	{3,  15},	{2,10},	    {2,15},	    {1,10},		{1,15},		{1, 255}  },
  {{3,20 },	   	{3, 16},	{2,20},	    {2,16},	    {1,20},		{1,16},		{1, 255}  },
  {{3,5 },   	{3,  8},	{2,5 },	    {2, 8},	    {1,5},		{1,8 },		{1, 255}  },
  {{3,12 },	   	{3, 11},	{2,12},	    {2,11},	    {1,12},		{1,11},		{1,25}  },
  {{3,9 },   	{3, 14},	{2,10},	    {2,14},	    {1,9},		{1,14},		{2,25}  }
};
#else
const Throw SETUP_MATRIX[0][0];
#endif



/**
 * @brief Describes points matrix and reads dartboard
 */
class Dartboard{
public:
    const uint8_t (*pins_master)[NUM_LINES_MASTER];
    const uint8_t (*pins_slave)[NUM_LINES_SLAVE];

    Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE]);


    /**
     * @brief Read hit dartboard
     * @return Throw hit place
     */
    const Throw ReadThrow();

    /**
     * @brief Set pinModes
     */
    void Init();
};



#endif