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
                        hit = ReadDartboard();
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
                
                    if(this->playerList[i].attempts == 0)
                            this->playerList[i].attempts = 255;
                            
                    SendToServer();
                    Serial.println();
                }
                
            }
        ++(this->round);
    }
    return this->status;
}