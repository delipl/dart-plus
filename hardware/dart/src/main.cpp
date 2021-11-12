#include <Arduino.h>
#include <stdint.h>
#include "config.h"

#include "player.h"

Dartboard dartboard(&pins_master, &pins_slave);

void setup() {
    Serial.begin(9600);
    dartboard.Init();

    Player deli(&dartboard, 1, "Jakub Delicat", "name");
}

void loop() {
    Throw hit = dartboard.ReadThrow();
    if(hit != Throw(0,0))
        Serial.println(hit);

    delay(100);
}