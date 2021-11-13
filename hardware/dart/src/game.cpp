#include "game.h"
Settings::Settings(const uint16_t &id, const uint8_t &amoutOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, Vector<uint16_t> & playersId):
id{id}, amoutOfPlayers{amoutOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}, playersId{playersId}{
    for(int i = 0; i < amoutOfPlayers; ++i){
        Serial.println(String("dodaje player id:") + String(this->playersId[i]));
        delay(100);
    }
}

Game::Game(const Settings &set): id{set.id}, settings{set}{   
    this->playerList = Vector<Player>(this->tab);
    Serial.println(this->settings.amoutOfPlayers);
    for(int i = 0; i < this->settings.amoutOfPlayers; ++i){
        this->playerList.push_back( Player(this->settings.playersId[i], String(this->settings.playersId[i]).c_str(), settings.startPoints, 0));
        // Serial.print("id: ");
        // Serial.print(this->playerList[i].id);
        // Serial.print("\tname: ");
        // Serial.print(this->playerList[i].nick);
        // Serial.print("\tpoints: ");
        // Serial.print(this->playerList[i].points);
        // Serial.print("\attemps: ");
        // Serial.println(this->playerList[i].attemps);
        Serial.println(this->playerList[i].Serialize());
        Serial.println("DUPA");
        delay(100);
    }

}

GameStatus Game::Loop(){
    Serial.println("Welcome to Dart-Plus");
    while(this->status != GameStatus_Finished){
        for(int i = 0; i < this->settings.amoutOfPlayers; ++i){
            this->playerList[i].attemps = 3;
            // Serial.println("Throws: " + this->playerList[i].nick);
            
            // Serial.println("\tPoints: "  + String(this->playerList[i].points));

            while(this->playerList[i].attemps != 0){
                while(this->status == GameStatus_Pause);

                Serial.println("\nLet's throw...");
                auto state = this->playerList[i].Throwing();
                while(state != ThrowStatus_OK){
                    state = this->playerList[i].Throwing();
                    // Serial.println(sizeof(this->playerList[i].Throwing()));
                }
                // Serial.println(sizeof(this->playerList[i].Throwing()));
                Serial.println(this->playerList[i].Serialize());
                Serial.println("Hit!");

                if(state == ThrowStatus_ERROR){
                    Serial.println("To much");
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
        }
    }
    return this->status;
}