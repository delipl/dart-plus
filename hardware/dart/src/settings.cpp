#include "settings.h"

Settings::Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t *playersId):
id{id}, amountOfPlayers{amountOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    //TODO: save playerIDS
    // for(int i = 0; i < amountOfPlayers; ++i){
    //     // Serial.println(String("Add player id:") + String(this->playersId[i]));
    //     delay(100);
    // }
}
