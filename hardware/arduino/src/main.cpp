#include <Arduino.h>
#include <stdint.h>
#include <ArduinoJson.h>
#include <SoftwareSerial.h>
#include <stdlib.h>
#include "config.h"
#include "dartboard.h"

Dartboard dartboard(&pins_master, &pins_slave);
SoftwareSerial EspSerial(A5, A4);  // RX, TX

void setup() {
    // Serial.begin(115200);
    Serial.begin(9600);
    EspSerial.begin(9600);
    Serial.println("\nInitiating dartboard...");
    dartboard.Init();
}

void loop() {
    Throw hit = dartboard.ReadThrow();
    if(not hit)
        return;
    EspSerial.print(hit.multiplier);
    EspSerial.print("\t");
    EspSerial.println(hit.value);

    Serial.print(hit.multiplier);
    Serial.print("\t");
    Serial.println(hit.value);
    delay(50);
}