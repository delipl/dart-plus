#include "settings.h"

Settings::Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t playersId[MAX_PLAYERS]):
id{id}, amountOfPlayers{amountOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    
    for(int i = 0; i < this->amountOfPlayers; ++i){
        this->playersId[i] = playersId[i];
        
    } 
}
