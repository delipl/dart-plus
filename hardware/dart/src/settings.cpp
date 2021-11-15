#include "settings.h"

Settings::Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t playersId[MAX_PLAYERS]):
id{id}, amountOfPlayers{amountOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    
    for(int i = 0; i < this->amountOfPlayers; ++i){
        this->playersId[i] = playersId[i];
        
    } 
}

StaticJsonDocument<SIZE_PLAYER_JSON> Settings::Document(){
    StaticJsonDocument<SIZE_PLAYER_JSON> doc;
    //JsonObject obj = doc.createNestedObject();

    doc["id"]                      = this->id;
    doc["amountOfPlayers"]         = this->amountOfPlayers;
    doc["startPoints"]             = this->startPoints;
    doc["doubleIn"]                = this->doubleIn;
    doc["doubleOut"]               = this->doubleOut;
    doc["playersId"][0] = 1;
    doc["playersId"][1] = 2;
    doc["playersId"][2] = 3;
    doc["playersId"][3] = 1;
    doc["playersId"][4] = 5;
    doc["playersId"][5] = 1;
    doc["playersId"][6] = 1;
    doc["playersId"][7] = 6;
    doc["playersId"][8] = 1;
    doc["playersId"][9] = 1;


    // for(int i = 0; i < MAX_PLAYERS; ++i){
    //         doc["playersId"][i] = 2;//this->playersId[i];
    //         Serial.println(this->playersId[i]);
    //     }


    return doc;
}

// void Settings::Deserialize(const StaticJsonDocument<SIZE_PLAYER_JSON> &doc){
//     //TODO:
//     serializeJson(doc, this->json); // -< do wyjebania
//     this->id = doc[0];
//     strcpy(this->nick, (const char*)doc[1]); // -< do wyjebania
//     this->points = doc[2];
//     this->attemps = doc[3];
// }