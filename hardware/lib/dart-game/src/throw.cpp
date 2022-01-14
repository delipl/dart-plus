#include "throw.h"

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
