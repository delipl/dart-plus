#include "game-api.h"


GameStatus GameApi::Tick(){

    Throw hit(0,0);
        for(int i = 0; i < this->settings.numberOfPlayers; ++i){
            this->playerList[i].attempts = 3;
            Serial.print("Throws: " );
            Serial.println(this->playerList[i].nick);
            this->throwingPlayerId = this->playerList[i].id;
            
         

            while(this->playerList[i].attempts != 0){
                //TODO: when button arrived
                
                while(this->status == GameStatus_Pause);

                Serial.println("\nLet's throw...");
                hit = Throw(0,0);
                while(hit == Throw(0,0)){
                    hit = dartboard.ReadThrow();
                }
                this->value = hit.value;
                this->multiplier = hit.multiplier;

                // Serial.println("value:");
                Serial.println(hit.value);
                

                
                if(hit.value * hit.multiplier > this->playerList[i].points){
                    Serial.print("hit: \t");
                    Serial.print(hit.value);
                    Serial.print("points: \t");
                    Serial.print(this->playerList[i].points);
                    Serial.println("\tTo much");
                    this->playerList[i].attempts = 0;
                }
                else if(hit.value * hit.multiplier == this->playerList[i].points){
                    Serial.println("Finished");
                    this->status = GameStatus_Finished;
                    this->playerList[i].attempts = 0;
                }
                else{
                    this->playerList[i].points = this->playerList[i].points - hit;
                    Serial.println("OK");
                    --this->playerList[i].attempts;
                    Serial.print(this->playerList[i].attempts);
                }
            
                serializeJson(this->Document(), mySerial);
                // serializeJson(this->Document(), Serial);
                delay(200);
            }
            
        }
    ++(this->round);
    return this->status;
}