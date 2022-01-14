#include "dartboard.h"
#include "math.h"
Throw::Throw(const uint8_t &multiplier, const uint8_t &value):
    multiplier{multiplier}, value{value}
{
    // this->json = "";
}

Throw::Throw(){
    this->multiplier = 0;
    this->value = 0;
}
Throw &Throw::operator=(const Throw &other) {
    this->multiplier = other.multiplier;
    this->value = other.value;
    return *this;
}

bool Throw::operator==(const Throw &other) const {
    return this->multiplier == other.multiplier && this->value == other.value;
}

bool Throw::operator!=(const Throw &other) const {
    return this->multiplier != other.multiplier || this->value != other.value;
}

bool Throw::operator!() const {
    return this->multiplier == 0 || this->value == 0;
}

bool Throw::operator==(const int &other) const {
    return this->multiplier*this->value == other;
}

bool Throw::operator>(const int &other) const{
    return this->multiplier*this->value > other;
}
bool Throw::operator<(const int &other) const{
    return this->multiplier*this->value < other;
}

StaticJsonDocument<SIZE_THROW_JSON> Throw::Document() const{
    StaticJsonDocument<SIZE_THROW_JSON> doc;
    doc["multiplier"] = this->multiplier;
    doc["value"] = this->value;
    return doc;
}

uint16_t operator- (const uint16_t &points, const Throw &hit){
    return points - hit.multiplier*hit.value;
}

uint16_t operator+ (const uint16_t &points, const Throw &hit){
    return points + hit.multiplier*hit.value;
}

Dartboard::Dartboard(const uint8_t (*pins_master)[NUM_LINES_MASTER], const uint8_t (*pins_slave)[NUM_LINES_SLAVE]){
    this->pins_master = pins_master;
    this->pins_slave = pins_slave;
}

void Dartboard::Init(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        pinMode(((*this->pins_master)[i]), OUTPUT);
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