#include "player.h"

Player::Player(const uint32_t &id, const String &nick, const uint16_t &points, const uint8_t &attemps):
id{id}, nick{nick}, points{points}, attemps{attemps}{

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
    Serial.println("Usuwam");
    this->points = this->points - hit;
    this->lastThrow = hit;
    if(this->points == 0)
        return ThrowStatus_END;
    return ThrowStatus_OK;
}

String operator+(const String &prefix, const Player &player){
    String x = prefix;
    if(prefix.substring(0,2) != "\t") x = "";
    return  prefix + "\n{\n" +
            x + "\t\"id\": " + String(player.id) + "\",\n"+
            x + "\t\"nick\": \"" + player.nick + "\",\n" +
            x + "\t\"points\": " + String(player.points) + ",\n" +
            x + "\t\"attemps\": " + String(player.attemps) +  ",\n" + 
            x + "\t\"lastThrow\": " + ("\t" + player.lastThrow) + 
            x + "\n}";
}

Player &Player::operator=(const Player &other){
    this->id = other.id;
    this->nick = other.nick;
    this->points = other.points;
    this->attemps = other.attemps;
    this->lastThrow = other.lastThrow;
    return *this;
}