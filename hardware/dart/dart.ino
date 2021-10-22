#include <stdint.h>
#include "config.h"

uint8_t pins_master[NUM_LINES_MASTER] = {2, 3, 4, 5, 11, 10, 9, 8, 7, 6};
uint8_t pins_slave[NUM_LINES_SLAVE] = {A5, 12, A4, 13, A3, A1, A2};

void setup() {
  Serial.begin(9600);
  
  for(uint8_t i=0; i<NUM_LINES_MASTER; i++) {
    pinMode(pins_master[i], OUTPUT);
    digitalWrite(pins_master[i], HIGH);
  }

  for(uint8_t i=0; i<NUM_LINES_SLAVE; i++)
    pinMode(pins_slave[i], INPUT_PULLUP);
}

void loop() {
  for(uint8_t i=0; i<NUM_LINES_MASTER; i++) {
    digitalWrite(pins_master[i], LOW);

    for(uint8_t j=0; j<NUM_LINES_SLAVE; j++) {
      if(!digitalRead(pins_slave[j])){

        Serial.println(GET_LOOKUP_VALUE(i, j));
        delay(500);

        break;
      }
    }

    digitalWrite(pins_master[i], HIGH);
  }
}
