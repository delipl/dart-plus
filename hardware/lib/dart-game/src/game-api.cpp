#include "game-api.h"

Throw GameApi::ReadDartboard(){
	while (Serial.available()==0) {} //Wait for user input
	const uint8_t multiplier = (Serial.readStringUntil('\t')).toInt();
	const uint8_t value = (Serial.readStringUntil('\n')).toInt();
	return Throw(multiplier,value);
}
// extern ServerClient *serverClient; 
void GameApi::SendDartboard(){
	// serverClient->SendGame(this->Document());
}

