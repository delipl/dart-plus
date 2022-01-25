#include "game.h"
Game::Game(const Settings &set) : id{set.id}, settings{set} {
    this->round = 0;
    this->multiplier = 0;
    this->value = 0;
}

StaticJsonDocument<SIZE_GAME_JSON> Game::Document() const{
    StaticJsonDocument<SIZE_GAME_JSON> doc;
    doc["id"] = this->id;
    doc["status"] = (uint8_t)this->status;
    doc["throwingPlayerId"] = this->throwingPlayerId;
    doc["multiplier"] = this->multiplier;
    doc["value"] = this->value;
    doc["round"] = this->round;
    uint16_t i = 0;
    for (const auto &player : settings.players) {
        doc["players"][i]["id"] = player->id;
        doc["players"][i]["nick"] = player->nick;
        doc["players"][i]["board_id"] = player->board_id;
        doc["players"][i]["points"] = player->points;
        doc["players"][i]["attempts"] = player->attempts;
        ++i;
    }
    return doc;
}

bool Game::Deserialize(const StaticJsonDocument<SIZE_GAME_JSON> &doc) {
    if(id != doc["id"]){
        // todo: error throw
        return false;
    }
    status = doc["status"];
    throwingPlayerId = doc["throwingPlayerId"];
    multiplier = doc["multiplier"];
    value = doc["value"];
    round = doc["round"];

    for (uint8_t i = 0; i < doc["players"].size(); ++i) {
        auto player = std::make_shared<Player>(doc["players"][i]["id"],
                         doc["players"][i]["nick"],
                         doc["players"][i]["board_id"]);
        player->attempts = doc["players"][i]["points"];
        player->points = doc["players"][i]["attempts"];
        if (not player->is_same(*settings.players[i])) {
            // todo: error throw
            return false;
        }
       player->attempts = player->attempts;
       player->points = player->points;
    }
    return true;
}

void Game::loop() {
        Throw hit(0, 0);
        for (auto &player : settings.players) {
            if(player->board_id != this_board_id){
                RequestGameLoop();
                continue;
            }

            player->attempts = 3;
            throwingPlayerId = player->id;
            while (player->attempts != 0) {
                while (status == GameStatus_Pause) {
                    // todo: request checking game status
                }

                hit = Throw(0, 0);
                while (hit == Throw(0, 0)) {
                    hit = ReadDartboard();
                }
                value = hit.value;
                multiplier = hit.multiplier;

                if(player->points == settings.startPoints && settings.doubleIn == true && hit.multiplier != 2){
                    --player->attempts;
                }
                else if (hit.value * hit.multiplier > player->points) {
                    player->attempts = 0;
                } else if (hit.value * hit.multiplier == player->points && settings.doubleOut == false) {
                    this->status = GameStatus_Finished;
                    player->attempts = 0;
                } else if (hit.value * hit.multiplier == player->points && settings.doubleOut == true && hit.multiplier == 2) {
                    this->status = GameStatus_Finished;
                    player->attempts = 0;
                } else {
                    player->points = player->points - hit;
                    --player->attempts;
                }
                SendDartboard();
            }
        }
        ++round;
}
