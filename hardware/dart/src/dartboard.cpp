#include "dartboard.h"
#include "math.h"
Throw::Throw(const uint8_t &multiplier, const uint8_t &value):
    multiplier{multiplier}, value{value}
{}

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

size_t Throw::write(const uint8_t *s, size_t n) {
    uint8_t sum = 0;
    for(size_t i = 0; i < n; ++i){
        uint8_t x = ((uint8_t)(s[i] - 48));
        // why just pow doesnt work
        for(size_t k = 0; k < n-i-1; ++k)
            x *= 10;
        sum += x;
    }
    *ptr = sum;
    ++ptr;
    return n;
};
size_t Throw::write(uint8_t c) { return 1;}
// JSON

String Throw::Serialize() const{
    StaticJsonDocument<16> doc;
    doc["multiplier"]   = this->multiplier;
    doc["value"]        = this->value;
    String out;
    serializeJson(doc, out);
    serializeJson(doc, Serial);
    return out;
}

void Throw::Deserialize(const StaticJsonDocument<16> &doc){
    ptr = (uint8_t*)this;
    serializeJson(doc, *this);
}


String operator+(const String &prefix, const Throw &hit){
    String x = prefix;
    if(prefix.substring(0,2) != "\t") x = "";
    return  prefix + "{\n" + 
            x + "\t\"multiplier\": " + String(hit.multiplier + String(",\n" + 
            x + "\t\"value\": ")) + String(hit.value) + String("\n "+ 
            x + "}");

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
        // Serial.println((*this->pins_master)[i]);
        pinMode(((*this->pins_master)[i]), OUTPUT);
        digitalWrite((*this->pins_master)[i], HIGH);
    }

    for(uint8_t i = 0; i < NUM_LINES_SLAVE; ++i){
        // Serial.println((*this->pins_slave)[i]);
        pinMode((*this->pins_slave)[i], INPUT_PULLUP);
    }
}

const Throw Dartboard::ReadThrow(){
    for(uint8_t i = 0; i < NUM_LINES_MASTER; ++i) {
        digitalWrite((*this->pins_master)[i], LOW);

        for(uint8_t j = 0; j < NUM_LINES_SLAVE; ++j) {
            // Pins A7 and A6 in Arduino Nano doesn't have GPIO Input Interface
            // Serial.print("Sprawdzam ");
            // Serial.println((*this->pins_slave)[j]);
            if((*this->pins_slave)[j] == A7 || (*this->pins_slave)[j] == A6){
                
                if(analogRead(A6) < 500 || analogRead(A7) < 500){
                    digitalWrite((*this->pins_master)[i], HIGH);
                    return SETUP_MATRIX[i][j];
                }
                continue;
        }
        
        if(!digitalRead((*this->pins_slave)[j])){
            return SETUP_MATRIX[i][j];
        }
    }
    digitalWrite((*this->pins_master)[i], HIGH);
  }
  return Throw(0, 0);
}