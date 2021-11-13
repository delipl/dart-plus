#include "game.h"
Settings::Settings(const uint16_t &id, const uint8_t &amoutOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, uint16_t playersId[]):
id{id}, amoutOfPlayers{amoutOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}{
    this->playersId = (uint16_t*)malloc(sizeof(uint16_t)*amoutOfPlayers);
    for(int i = 0; i < amoutOfPlayers; ++i)
        this->playersId[i] = playersId[i];
}

Game::Game(const Settings &set): id{set.id}, settings{set}{
    this->playerList = (Player*)malloc(sizeof(Player)*this->settings.amoutOfPlayers);
    for(int i = 0; i < settings.amoutOfPlayers; ++i)
        this->playerList[i] = Player(i, String("Player #") + String(i), settings.startPoints, 0);
}

GameStatus Game::Loop(){
    for(int i = 0; i < this->settings.amoutOfPlayers; ++i){
        this->playerList[i].attemps = 3;

        while(this->playerList[i].attemps != 0){
            auto state = this->playerList[i].Throwing();
            
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