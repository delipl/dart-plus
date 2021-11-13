#include "game.h"
Settings::Settings(const uint16_t &id, const uint8_t &amoutOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, const Vector<uint16_t> & playersId):
id{id}, amoutOfPlayers{amoutOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}, playersId{playersId}{
    for(int i = 0; i < amoutOfPlayers; ++i){
        // this->playersId.push_back(playersId[i]);
        Serial.println(String("dodaje player id:") + String(this->playersId[i]));
        delay(100);
    }
}

Game::Game(const Settings &set): id{set.id}, settings{set}{
    Vector<Player> vec(this->playerList);
   
    for(int i = 0; i < settings.amoutOfPlayers; ++i)
        vec.push_back(Player(i, String("Player #") + String(i), settings.startPoints, 0));
}

GameStatus Game::Loop(){
    Serial.println("Welcome to Dart-Plus");
    while(this->status != GameStatus_Finished){
        for(int i = 0; i < this->settings.amoutOfPlayers; ++i){
            this->playerList[i].attemps = 3;
            Serial.println("Throws: " + this->playerList[i].nick);
            
            Serial.println("\tPoints: "  + String(this->playerList[i].points));

            while(this->playerList[i].attemps != 0){
                while(this->status == GameStatus_Pause);

                Serial.println("Let's throw...");
                // while((state = this->playerList[i].Throwing()) != )
                auto state = this->playerList[i].Throwing();
                while(state != ThrowStatus_OK)
                    state = this->playerList[i].Throwing();
                Serial.println("Hit!");
                Serial.println("\t"+this->playerList[i].lastThrow);

                // Serial.println(String("player") + this->playerList[i]);
                if(state == ThrowStatus_ERROR){
                    Serial.println("To much");
                    this->playerList[i].points = this->playerList[i].points + this->playerList[i].lastThrow;
                    this->playerList[i].attemps = 0;
                }
                else if(state == ThrowStatus_END){
                    Serial.println("Finished");
                    this->status = GameStatus_Finished;
                    this->playerList[i].attemps = 0;
                }
                else{
                    Serial.println("OK");
                    --this->playerList[i].attemps;
                }
                delay(100);
            }

            // if(this->status == GameStatus_Finished){
            //     Serial.println("Finished OUT");
            //     break;
            // }
        }
    }
    return this->status;
}