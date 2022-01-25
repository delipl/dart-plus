#include "game-api.h"

Throw GameApi::ReadDartboard() const{
	//while (Serial.available()==0) {} //Wait for user input
    uint8_t multiplier = 0;
    uint8_t value = 0;
    while (multiplier == 0 && value == 0){
        client->loop();
        multiplier = (Serial.readStringUntil('\t')).toInt();
        value = (Serial.readStringUntil('\n')).toInt();
    }

    Serial.println(multiplier);
    Serial.println(value);
    // const uint8_t multiplier = 3;
    // const uint8_t value = 3;
	return Throw(multiplier,value);
}

void GameApi::SendDartboard() const{
	client->SendGame(this->Document());
}

void GameApi::RequestGameLoop(){
    // serverClient
}