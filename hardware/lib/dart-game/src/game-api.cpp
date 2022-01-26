#include "game-api.h"

Throw GameApi::ReadDartboard() const{

    auto x = Throw(rand()%3 +1,rand()%10+1);
    delay(2000);
    // USE_SERIAL.printf("[GAMELOOP] Thowing [%d, %d]\n", x.multiplier, x.value);
    return x;
}

void GameApi::SendDartboard() const{
    String raw;
    serializeJson(Document(), raw);
    client->SendGame(raw);
}

void GameApi::RequestGameLoop(){
    // serverClient
}