#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#include "config.h"
// #include "settings.h"
#include "game.h"


#define SERVER_IP "http://192.168.192.3:8000/"

#ifndef STASSID
	#define STASSID "Play internet 4G LTE-D87FD9"
	#define STAPSK "1mF5yX7j"
#endif


Settings settings;


void setup()
{
	Serial.begin(9600);

	String mess;
	// waiting for settings message
	while (mess == String()){
		mess = Serial.readString();
	}		

	const char *get = mess.c_str();
	StaticJsonDocument<SIZE_SETTINGS_JSON> doc;
	deserializeJson(doc, get);
	settings.Deserialize(doc);
	serializeJsonPretty(doc, Serial);

	

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
	}
}