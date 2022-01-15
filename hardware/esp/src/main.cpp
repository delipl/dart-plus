#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#include "config.h"
#include "server-client.h"

#include "game-api.h"



#define SERVER_IP "http://192.168.0.3:8000/games"

#ifndef STASSID
	#define STASSID "multimedia_plastek"
	#define STAPSK "123454321"
#endif

uint16_t ids[] = {1,2,3,4};
Settings settings(1, 4, 301, false, false, ids);
ServerClient *serverClient;

GameApi game(settings);

void setup()
{
	Serial.begin(9600);
	serverClient = new ServerClient(STASSID, STAPSK, SERVER_IP);
	serverClient->SendSettings(settings.Document());

}

void loop(){

	game.Loop();
	// Game game(settings);
	// while(true){

	// 	String mess;
	// 	// waiting for settings message
	// 	while (mess == String()){
	// 		mess = Serial.readString();
	// 	}		

	// 	const char *get = mess.c_str();
	// 	StaticJsonDocument<SIZE_GAME_JSON> doc;
	// 	deserializeJson(doc, get);
	// 	game.Deserialize(doc);
	// 	serializeJsonPretty(game.Document(), Serial);

	// 	serverClient->SendGame(game.Document());
	// }
}

