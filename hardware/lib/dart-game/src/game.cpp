#include "game.h"
Game::Game(const Settings &set): id{set.id}, settings{set}{   
    // Serial.println(this->settings.numberOfPlayers);

    // // this->playerList = new Player[this->settings.numberOfPlayers];
    // for(int i = 0; i < this->settings.numberOfPlayers; ++i){
    //     Serial.print("Loaded: ");
    //     Serial.println(this->settings.playersId[i]);
    // }

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


    for(uint8_t i = 0; i < this->settings.numberOfPlayers; ++i){
        doc["playerList"][i]["id"] = this->playerList[i].id;
        doc["playerList"][i]["atempts"] = this->playerList[i].attemps;
        doc["playerList"][i]["points"] = this->playerList[i].points;
    }
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
        this->playerList[i].id = doc["playerList"][i]["id"];
        this->playerList[i].attemps = doc["playerList"][i]["atempts"];
        this->playerList[i].points =doc["playerList"][i]["points"];
    }
}