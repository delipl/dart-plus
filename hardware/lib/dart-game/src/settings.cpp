#include "settings.h"
// Settings::Settings() : id(0),
//                        startPoints{0},
//                        doubleIn{false},
//                        doubleOut{false} {
// }

Settings::Settings(const uint16_t &id, const uint16_t &startPoints, const bool &doubleIn, const bool &doubleOut, const std::initializer_list<std::shared_ptr<Player>> &list) : id{id}, startPoints{startPoints}, doubleIn{doubleIn}, doubleOut{doubleOut} {
    // players.insert(this->players.end(), list.begin(), list.end());
    for (const auto &elem : list)
        players.push_back(elem);
}

StaticJsonDocument<SIZE_SETTINGS_JSON> Settings::Document(){
    StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
    doc["id"]                      = this->id;
    doc["startPoints"]             = this->startPoints;
    doc["doubleIn"]                = this->doubleIn;
    doc["doubleOut"]               = this->doubleOut;
    uint16_t i = 0;
    for(const auto &player : players){
        doc["players"][i]["id"] = player->id;
        doc["players"][i]["boardId"] = player->board_id;
        doc["players"][i]["nick"] = player->nick;
        ++i;
    }

    return doc;
}

Settings::Settings(const  StaticJsonDocument<SIZE_SETTINGS_JSON> &doc):
id{doc["id"]}, startPoints{doc["startPoints"]}, doubleIn{doc["doubleIn"]},doubleOut{doc["doubleOut"]}{
    for (size_t i = 0; i < doc["players"].size(); ++i)
        players.push_back(std::make_shared<Player>(doc["players"][i]["id"], doc["players"][i]["board_id"], doc["players"][i]["nick"]));
}