#include "player.h"

Player::Player(const uint16_t &id, const String &nick, const uint16_t &points, const uint8_t &attemps):
id{id}, nick{nick}, points{points}, attemps{attemps}{
    this->json = "";
}
Player::Player():id{0}, nick{"\0"}, points{0}, attemps{0}{}

const ThrowStatus Player::Throwing(){
    Throw hit(0,0); 
    while(hit == Throw(0,0)){
        hit = dartboard.ReadThrow();
        // Serial.println("\t" + hit);
    }
    if (hit > this->points)
        return ThrowStatus_ERROR;
    this->points = this->points - hit;
    this->lastThrow = hit;
    if(this->points == 0)
        return ThrowStatus_END;
    return ThrowStatus_OK;
}

Player &Player::operator=(const Player &other){
    this->id = other.id;
    this->nick = other.nick;
    this->points = other.points;
    this->attemps = other.attemps;
    this->lastThrow = other.lastThrow;
    return *this;
}

String Player::Serialize() const{
    StaticJsonDocument<SIZE_PLAYER_JSON> doc;
    doc["id"]           = this->id;
    doc["nick"]         = this->nick;
    doc["points"]       = this->points;
    doc["attemps"]      = this->attemps;

    String temp = this->json;
    serializeJson(doc, temp);
    return this->json;
}

void Player::Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc){
    serializeJson(doc, this->json);
    this->id = doc[0];
    this->nick = (const char*)doc[1];
    this->points = doc[2];
    this->attemps = doc[3];
}