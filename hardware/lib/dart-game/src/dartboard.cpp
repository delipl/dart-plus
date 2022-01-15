#include "dartboard.h"
#include "math.h"
Dartboard::Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE]){
    this->pins_master = pins_master;
    this->pins_slave = pins_slave;
    this->button = 13;
}

void Dartboard::Init(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        pinMode(((*this->pins_master)[i]), OUTPUT);
        //przycisk zmiany gracza
        pinMode(button, INPUT_PULLUP);
        digitalWrite((*this->pins_master)[i], HIGH);
        // Serial.print("Ustawiam pin: ");
        // Serial.println((*this->pins_master)[i]);
    }

    
    for(uint8_t i = 0; i < NUM_LINES_SLAVE; ++i){
        if((*this->pins_slave)[i] != A7 && (*this->pins_slave)[i] != A6) 
            pinMode((*this->pins_slave)[i], INPUT_PULLUP);
        // pinMode((*this->pins_slave)[i], INPUT_PULLUP);
    }
}

const Throw Dartboard::ReadThrow(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        digitalWrite((*this->pins_master)[i], HIGH);
    }

    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        digitalWrite((*this->pins_master)[i], LOW);

        for(uint8_t j = 0; j < NUM_LINES_SLAVE; ++j) {
            // Pins A7 and A6 in Arduino Nano doesn't have GPIO Input Interface
            if((*this->pins_slave)[j] == A7 ){
                if(analogRead(A7) < 500){
                    digitalWrite((*this->pins_master)[i], HIGH);
                    return SETUP_MATRIX[i][j];
                }
            }else if((*this->pins_slave)[j] == A6){
                if(analogRead(A6) < 500){
                    digitalWrite((*this->pins_master)[i], HIGH);
                    return SETUP_MATRIX[i][j];
                }
            }
            else if(digitalRead((*this->pins_slave)[j]) == 0){
                return SETUP_MATRIX[i][j];
            }
        }
        digitalWrite((*this->pins_master)[i], HIGH);
    }
  
  return Throw(0, 0);
}