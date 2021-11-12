#include "player.h"

Player::Player(Dartboard * dartboard, const uint32_t &id, const String &name, const String &nick, const uint16_t &points, const uint8_t &attemps):
dartboard{dartboard}, id{id}, name{name}, nick{nick}, points{points}, attemps{attemps}{

}

const Throw Player::Throwing(){
    return dartboard->ReadThrow();
}