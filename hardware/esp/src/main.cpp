#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#include "config.h"
#include "game.h"
#include "server-client.h"


#define SERVER_IP "http://192.168.192.3:8000/games"

#ifndef STASSID
	#define STASSID "Play internet 4G LTE-D87FD9"
	#define STAPSK "1mF5yX7j"
#endif


Settings settings;
ServerClient *serverClient;

void setup()
{
	Serial.begin(9600);

	String mess;
	serverClient = new ServerClient(STASSID, STAPSK, SERVER_IP);
	delay(1000);
	// waiting for settings message
	while (mess == String()){
		mess = Serial.readString();
	}		

	const char *get = mess.c_str();
	StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
	deserializeJson(doc, get);
	settings.Deserialize(doc);
	serializeJsonPretty(doc, Serial);
	delay(100);
	serverClient->SendJson(doc);
	

	

}

void loop(){
	Game game(settings);
	while(true){

		String mess;
		// waiting for settings message
		while (mess == String()){
			mess = Serial.readString();
		}		

		const char *get = mess.c_str();
		StaticJsonDocument<SIZE_GAME_JSON> doc;
		deserializeJson(doc, get);
		game.Deserialize(doc);
		serializeJsonPretty(game.Document(), Serial);
		serverClient->SendJson(doc);
	}
}