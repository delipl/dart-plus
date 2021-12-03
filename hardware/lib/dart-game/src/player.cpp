#include "player.h"

Player::Player(const uint16_t &id, const char nick[NICK_LENGTH], const uint16_t &points, const uint8_t &attemps):
id{id}{
    strcpy(this->nick, nick);
    this->points = points;
    this->attemps = attemps;
}
Player::Player():id{0}, nick{"nick"}, points{0}, attemps{0}{
}


Player &Player::operator=(const Player &other){
    this->id = other.id;
    this->points = other.points;
    this->attemps = other.attemps;
    return *this;
}

StaticJsonDocument<SIZE_PLAYER_JSON> Player::Document(){
    StaticJsonDocument<SIZE_PLAYER_JSON> doc;
    doc["id"]           = this->id;
    doc["nick"]         = this->nick;
    doc["attemps"]      = this->attemps;
    return doc;
}


void Player::Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc){
    this->id = doc[0];
    this->points = doc[2];
    this->attemps = doc[3];
}