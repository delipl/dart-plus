#ifndef THROW_H
#define THROW_H
#include "Arduino.h"
#include "ArduinoJson.h"
// REMOVE THIS
#include "config.h"
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
    Throw();
    StaticJsonDocument<SIZE_THROW_JSON> Document() const;
};
uint16_t operator- (const uint16_t &points, const Throw &hit);
uint16_t operator+ (const uint16_t &points, const Throw &hit);

#endif