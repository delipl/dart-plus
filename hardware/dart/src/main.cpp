#include <Arduino.h>
#include <stdint.h>
#include "config.h"
#include "dartboard.h"

Dartboard dartboard(&pins_master, &pins_slave, &matrix_lookup);

void setup() {
    Serial.begin(9600);
    dartboard.Init();
  
}

void loop() {
    auto hit = dartboard.ReadThrow();
    // Serial.print("Sprawdzam");
    if(hit.multiplier){
        Serial.print(hit.multiplier);
        Serial.print("\t");
        Serial.println(hit.value);

    }
    delay(500);
}