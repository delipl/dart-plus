#include "game-api.h"

Throw GameApi::ReadDartboard(){
	//while (Serial.available()==0) {} //Wait for user input
    uint8_t multiplier = 0;
    uint8_t value = 0;
    while (multiplier == 0 && value == 0){
        multiplier = (Serial.readStringUntil('\t')).toInt();
	    value = (Serial.readStringUntil('\n')).toInt();
    }

    Serial.println(multiplier);
    Serial.println(value);
    // const uint8_t multiplier = 3;
    // const uint8_t value = 3;
	return Throw(multiplier,value);
}
extern ServerClient *serverClient; 
void GameApi::SendDartboard(){
	serverClient->SendGame(this->Document());
}

