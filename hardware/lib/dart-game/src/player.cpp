#include "player.h"

Player::Player(const uint16_t &id, const uint16_t &board_id, const std::string &nick, const uint16_t &points) : 
id(id), board_id(board_id), nick(nick), points(points) {
}

Player::Player() : id(0), board_id(0), nick("unknown"), points(0) {
}

Player::Player(const Player &other):
id(other.id), board_id(other.board_id), nick(other.nick), points(other.points){
}


bool Player::is_same(const Player &player) const{
    if (id != player.id)
        return false;
    if (nick != player.nick)
        return false;
    if (board_id != player.board_id) 
        return false;
    return true;
}