#include "settings.h"

Settings::Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t playersId[MAX_PLAYERS]):
id{id}, amountOfPlayers{amountOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    
    for(int i = 0; i < this->amountOfPlayers; ++i){
        this->playersId[i] = playersId[i];
        
    } 
}

StaticJsonDocument<SIZE_SETTINGS_JSON> Settings::Document(){
    StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
    
    doc["id"]                      = this->id; 
    doc["amountOfPlayers"]         = this->amountOfPlayers;
    doc["startPoints"]             = this->startPoints;
    doc["doubleIn"]                = this->doubleIn;
    doc["doubleOut"]               = this->doubleOut;

    for(int i = 0; i < this->amountOfPlayers; ++i){
            doc["playersId"][i] = this->playersId[i];
        }


    return doc;
}

void Settings::Deserialize(StaticJsonDocument<SIZE_SETTINGS_JSON> &doc){
    
    this->id = doc["id"];
    this->amountOfPlayers = doc["amountOfPlayers"];
    this->startPoints = doc["startPoints"];
    this->doubleIn = doc["doubleIn"];
    this->doubleOut = doc["doubleOut"];

    for(int i = 0; i < this->amountOfPlayers; ++i){
            this->playersId[i] = doc["playersId"][i];
        }
}