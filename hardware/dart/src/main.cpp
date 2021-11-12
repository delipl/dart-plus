#include <Arduino.h>
#include <stdint.h>
#include "config.h"

#include "player.h"

Dartboard dartboard(&pins_master, &pins_slave);
Player deli(&dartboard, 1, "Jakub Delicat", "deli");
void setup() {
    Serial.begin(9600);
    dartboard.Init();
}

void loop() {
    if(deli.Throwing() == ThrowStatus_OK)
        Serial.println(String("\"player\":") +deli);

    delay(500);
}