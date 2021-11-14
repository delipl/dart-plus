#include "game.h"
Settings::Settings(const uint16_t &id, const uint8_t &amountOfPlayers, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, Vector<uint16_t> & playersId):
id{id}, amountOfPlayers{amountOfPlayers}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut}, playersId{playersId}{
    for(int i = 0; i < amountOfPlayers; ++i){
        // Serial.println(String("Add player id:") + String(this->playersId[i]));
        delay(100);
    }
}

Game::Game(const Settings &set): id{set.id}, settings{set}{   
    Serial.println(this->settings.amountOfPlayers);
    this->playerList = new Player[this->settings.amountOfPlayers];
    // for(int i = 0; i < this->settings.amountOfPlayers; ++i){
    //     Serial.print("Loaded: ");
    //     Serial.println(this->settings.playersId[i]);
    // }

    for(int i = 0; i < set.amountOfPlayers; ++i){
        this->playerList[i] = Player(i, String("Player #" + String(i)).c_str(), settings.startPoints, UINT8_MAX);
    }
}

GameStatus Game::Loop(){
    Serial.println("Welcome to Dart-Plus");
    while(this->status != GameStatus_Finished){
        for(int i = 0; i < this->settings.amountOfPlayers; ++i){
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

Game::~Game(){
    delete[] playerList;
}

StaticJsonDocument<SIZE_GAME_JSON> Game::Document(){
    StaticJsonDocument<SIZE_GAME_JSON> doc;
    doc["id"]               = this->id;
    doc["status"]           = this->status;
    doc["throwingPlayerId"] = this->throwingPlayerId;
    doc["round"]            = this->round;

    for(int i = 0; i < this->settings.amountOfPlayers; ++i){
        //TODO:
        // INSERT DOC INTO DOC
        for(size_t j = 0; j < this->playerList[i].Document().size(); ++j){
            doc["playerList"][i]["id"] = this->playerList[i].Document()["id"];
            doc["playerList"][i]["points"] = this->playerList[i].Document()["points"];
            doc["playerList"][i]["attemps"] = this->playerList[i].Document()["attemps"];
        }
    }
    return doc;
}

void Game::Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc){
    // serializeJson(doc, this->json);
    // this->id = doc[0];
    // strcpy(this->nick, (const char*)doc[1]);
    // this->points = doc[2];
    // this->attemps = doc[3];
}