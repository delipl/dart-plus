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
   
    for(int i = 0; i < settings.amoutOfPlayers; ++i){
        vec.push_back(Player(i, String("Player #") + String(i), settings.startPoints, 0));
        Serial.println(String("dodaje player do gry: ") + this->playerList[i].id);
    }
}

GameStatus Game::Loop(){
    for(int i = 0; i < this->settings.amoutOfPlayers; ++i){
        this->playerList[i].attemps = 3;

        while(this->playerList[i].attemps != 0){
            auto state = this->playerList[i].Throwing();
            Serial.println(String("player") + this->playerList[i]);
            if(state == ThrowStatus_ERROR){
                this->playerList[i].points = this->playerList[i].points + this->playerList[i].lastThrow;
                this->playerList[i].attemps = 0;
            }
            else if(state == ThrowStatus_END){
                this->status = GameStatus_Finished;
                this->playerList[i].attemps = 0;
            }
            else{
                --this->playerList[i].attemps;
            }
        }

        if(this->status == GameStatus_Finished)
            break;
    }
    return this->status;
}