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

    #ifdef ARDUINO_CONFIG
        doc[0]               = this->id;
        doc[1]           = (uint8_t)this->status;
        doc[2] = this->throwingPlayerId;
        doc[3]       = this->multiplier;
        doc[4]            = this->value;
        doc[5]            = this->round;
        for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
            doc[6][i][0] = this->playerList[i].id;
            doc[6][i][1] = this->playerList[i].attempts;
            doc[6][i][2] = this->playerList[i].points; 
        }
    #endif

    #ifdef ESP_CONFIG
        doc["id"]               = this->id;
        doc["status"]           = (uint8_t)this->status;
        doc["throwingPlayerId"] = this->throwingPlayerId;
        doc["multiplier"]       = this->multiplier;
        doc["value"]            = this->value;
        doc["round"]            = this->round;
        for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
            doc["playerList"][i]["id"] = this->playerList[i].id;
            doc["playerList"][i]["attempts"] = this->playerList[i].attempts;
            doc["playerList"][i]["points"] = this->playerList[i].points;
        }
    #endif
    return doc;
}

void Game::Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc){ 
    this->id               = doc[0];
    this->status           = doc[1];
    this->throwingPlayerId = doc[2];
    this->multiplier       = doc[3];
    this->value            = doc[4];
    this->round            = doc[5];

    for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
        this->playerList[i].id = doc[6][i][0];
        this->playerList[i].attempts = doc[6][i][1];
        this->playerList[i].points =doc[6][i][2];
    }
}