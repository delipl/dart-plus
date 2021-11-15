#include "player.h"

Player::Player(const uint16_t &id, const char nick[NICK_LENGTH], const uint16_t &points, const uint8_t &attemps):
id{id}{
    strcpy(this->nick, nick);
    this->points = points;
    this->attemps = attemps;
    this->json = "";
}
Player::Player():id{0}, nick{"nick"}, points{0}, attemps{0}{
}

// TODO: To loop game
const ThrowStatus Player::Throwing(){
    Throw hit; 
    // TODO: don't make infinite loop
    while(dartboard.ReadThrow() == Throw(0,0)){
        hit = dartboard.ReadThrow();
        // Serial.println("\t" + hit);
    }

    // TODO: dont check error
    if (hit > this->points)
        return ThrowStatus_ERROR;

    this->points = this->points - hit;
    if(this->points == 0)
        return ThrowStatus_END;

    return ThrowStatus_OK;
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

String Player::Serialize(){
    StaticJsonDocument<SIZE_PLAYER_JSON> doc;
    doc["id"]           = this->id;
    doc["nick"]         = this->nick;
    doc["attemps"]      = this->attemps;

    serializeJson(doc, this->json);
    return this->json;
}

void Player::Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc){
    //TODO:
    
    serializeJson(doc, this->json); // -< do wyjebania
    this->id = doc[0];
    strcpy(this->nick, (const char*)doc[1]); // -< do wyjebania
    this->points = doc[2];
    this->attemps = doc[3];
}