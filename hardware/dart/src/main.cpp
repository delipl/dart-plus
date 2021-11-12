#include <Arduino.h>
#include <stdint.h>
#include "config.h"

#include "dartboard.h"

Dartboard dartboard(&pins_master, &pins_slave);

void setup() {
    Serial.begin(9600);
    dartboard.Init();

}

void loop() {
    Throw hit = dartboard.ReadThrow();
    // Serial.println(analogRead(A6));

    delay(100);
}