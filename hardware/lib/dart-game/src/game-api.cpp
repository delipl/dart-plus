#include "game-api.h"


GameStatus GameApi::Loop(){
    while(this->status != GameStatus_Finished){
        Throw hit(0,0);
            for(int i = 0; i < this->settings.numberOfPlayers; ++i){
                this->playerList[i].attempts = 3;
                this->throwingPlayerId = this->playerList[i].id;
                
                

                while(this->playerList[i].attempts != 255){                 
                    while(this->status == GameStatus_Pause);

                    // Serial.println("\nLet's throw...");
                    hit = Throw(0,0);
                    while(hit == Throw(0,0)){
                        hit = dartboard.ReadThrow();
                    }
                    this->value = hit.value;
                    this->multiplier = hit.multiplier;               

                    
                    if(hit.value * hit.multiplier > this->playerList[i].points){
                        // Serial.println("\tTo much");
                        this->playerList[i].attempts = 0;
                    }
                    else if(hit.value * hit.multiplier == this->playerList[i].points){
                        // Serial.println("Finished");
                        this->status = GameStatus_Finished;
                        this->playerList[i].attempts = 0;
                    }
                    else{
                        this->playerList[i].points = this->playerList[i].points - hit;
                        // Serial.println("OK");
                        --this->playerList[i].attempts;
                    }
                    if(this->playerList[i].attempts == 0){
                        this->playerList[i == this->settings.numberOfPlayers - 1 ? 0 : i + 1].attempts = 3;    
                    }
                
                    serializeJson(this->Document(), mySerial);
                    serializeJson(this->Document(), Serial);
                    if(this->playerList[i].attempts == 0)
                            this->playerList[i].attempts = 255;

                    Serial.println();
                    // for(int j = 0; j < this->settings.numberOfPlayers; ++j){
                    //     Serial.print(j + String("\t"));
                    //     Serial.println(this->playerList[j].points);
                    // }
                    delay(200);
                }
                
            }
        ++(this->round);
    }
    return this->status;
}