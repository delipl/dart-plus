#include "settings.h"
Settings::Settings():
id{0}, numberOfPlayers{0}, startPoints{301}, doubleIn{false}, doubleOut{false}
{
    for(int i = 0; i < this->numberOfPlayers; ++i)
        this->playersId[i] = 0;
        
    
}

Settings::Settings(const uint16_t &id, const uint8_t &numberOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t playersId[MAX_PLAYERS]):
id{id}, numberOfPlayers{numberOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    
    for(int i = 0; i < this->numberOfPlayers; ++i)
        this->playersId[i] = playersId[i];
        
}

StaticJsonDocument<SIZE_SETTINGS_JSON> Settings::Document(){
    StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
    
    doc["id"]                      = this->id; 
    doc["numberOfPlayers"]         = this->numberOfPlayers;
    doc["startPoints"]             = this->startPoints;
    doc["doubleIn"]                = this->doubleIn;
    doc["doubleOut"]               = this->doubleOut;

    for(int i = 0; i < this->numberOfPlayers; ++i){
        doc["playersId"][i] = this->playersId[i];
    }


    return doc;
}

void Settings::Deserialize(StaticJsonDocument<SIZE_SETTINGS_JSON> &doc){
    
    this->id = doc["id"];
    this->numberOfPlayers = doc["numberOfPlayers"];
    this->startPoints = doc["startPoints"];
    this->doubleIn = doc["doubleIn"];
    this->doubleOut = doc["doubleOut"];

    for(int i = 0; i < this->numberOfPlayers; ++i)
        this->playersId[i] = doc["playersId"][i];
}