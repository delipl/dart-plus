#include "game.h"
Game::Game(const Settings &set): id{set.id}, settings{set}{   
    for(int i = 0; i < set.numberOfPlayers; ++i){
        this->playerList[i] = Player(i, String("Player #" + String(i)).c_str(), settings.startPoints, 0);
    }

    this->throwingPlayerId = this->playerList[0].id;
    this->round = 0;
    this->multiplier = 0;
    this->value = 0;
}


StaticJsonDocument<SIZE_GAME_JSON> Game::Document(){
    StaticJsonDocument<SIZE_GAME_JSON> doc;

    doc["id"]               = this->id;
    doc["status"]           = (uint8_t)this->status;
    doc["throwingPlayerId"] = this->throwingPlayerId;
    doc["multiplier"]       = this->multiplier;
    doc["value"]            = this->value;
    doc["round"]            = this->round;

    #ifdef ARDUINO_CONFIG
        for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
            doc["playerList"][i][0] = this->playerList[i].id;
            doc["playerList"][i][1] = this->playerList[i].attemps;
            doc["playerList"][i][2] = this->playerList[i].points; 
        }
    #endif

    #ifdef ESP_CONFIG
        for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
            doc["playerList"][i]["id"] = this->playerList[i].id;
            doc["playerList"][i]["attempts"] = this->playerList[i].attemps;
            doc["playerList"][i]["points"] = this->playerList[i].points;
        }
    #endif
    return doc;
}

void Game::Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc){ 
    this->id               = doc["id"];
    this->status           = doc["status"];
    this->throwingPlayerId = doc["throwingPlayerId"];
    this->multiplier       = doc["multiplier"];
    this->value            = doc["value"];
    this->round            = doc["round"];

    for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
        this->playerList[i].id = doc["playerList"][i][0];
        this->playerList[i].attemps = doc["playerList"][i][1];
        this->playerList[i].points =doc["playerList"][i][2];
    }



}