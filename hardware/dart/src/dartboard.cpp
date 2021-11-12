#include "dartboard.h"

Throw::Throw(const uint8_t &multiplier, const uint8_t &value):
 multiplier{multiplier},value{value}
{}


Dartboard::Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE]){
    this->pins_master = pins_master;
    this->pins_slave = pins_slave;
    this->matrix_lookup = &SETUP_MATRIX;
}

void Dartboard::Init(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        pinMode(((*this->pins_master)[i]), OUTPUT);
        digitalWrite((*this->pins_master)[i], HIGH);
    }

    for(uint8_t i = 0; i < NUM_LINES_SLAVE; ++i)
        pinMode((*this->pins_slave)[i], INPUT_PULLUP);
}

const Throw Dartboard::ReadThrow(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        digitalWrite((*this->pins_master)[i], LOW);

        for(uint8_t j = 0; j < NUM_LINES_SLAVE; ++j) {
            // Pins A7 and A6 in Arduino Nano doesn't have GPIO Input Interface
            if((*this->pins_slave)[j] == A7 || (*this->pins_slave)[i] == A6){
                
                if(analogRead(A6) < 500 || analogRead(A7) < 500){
                    digitalWrite((*this->pins_master)[i], HIGH);
                    return (*this->matrix_lookup)[i][j];
                }
                continue;
        }
        
        if(!digitalRead((*this->pins_slave)[j])){
            digitalWrite((*this->pins_master)[i], HIGH);
            return (*this->matrix_lookup)[i][j];
        }
    }
    digitalWrite((*this->pins_master)[i], HIGH);
  }
  return Throw(0, 0);
}