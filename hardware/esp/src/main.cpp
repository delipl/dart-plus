#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define SERVER_IP "http://192.168.192.3:8000/"

#ifndef STASSID
#define STASSID "Play internet 4G LTE-D87FD9"
#define STAPSK  "1mF5yX7j"
#endif

void setup() {

  Serial.begin(115200);

  Serial.println();
  Serial.println();
  Serial.println();

  WiFi.begin(STASSID, STAPSK);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());


 // wait for WiFi connection
  if ((WiFi.status() == WL_CONNECTED)) {

    WiFiClient client;
    HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    http.begin(client, SERVER_IP+String("settings")); 
    http.addHeader("Content-Type", "application/json");

    Serial.print("[HTTP] POST...\n");
    // uint8_t jsonValues[108] = "{\"gameStatus\":1,\"maxThrow\":132,\"numberOfThrow\":12,\"round\":0,\"throwingPlayerId\":33}";
    // Serial.println((char*)jsonValues);
    String ID;// = String(random(0, UINT16_MAX));
     String json ;
      ID = String(random(0, UINT16_MAX));
      json = "{\"id\":" + ID  + ",\"numberOfPlayers\":4,\"startPoints\":65535,\"doubleIn\":true,\"doubleOut\":false,\"playersId\":[88,1,2,56]}";
      Serial.println(json);
      int httpCode = http.POST(json);

      if (httpCode > 0) {
        Serial.printf("[HTTP] POST... code: %d\n", httpCode);

        if (httpCode == HTTP_CODE_OK) {
          const String& payload = http.getString();
          Serial.println("received payload:\n<<");
          Serial.println(payload);
          Serial.println(">>");
        }
      } else {
        Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }



    // GAME STATUS

    

    Serial.print("[HTTP] PUT...\n");
    while(true){
      HTTPClient http1;

     Serial.print("[HTTP] begin...\n");
      http1.begin(client, SERVER_IP+String("games")); 
      http1.addHeader("Content-Type", "application/json");

      json = "{\"id\":" + ID + ",\"status\":0,\"throwingPlayerId\":2,\"multiplier\":3,\"value\":"+ String(random(0,301)) +",\"round\":2,\"playerList\":[{\"id\":1,\"attempts\":0,\"points\":100},{\"id\":2,\"attempts\":0,\"points\":228},{\"id\":3,\"attempts\":0,\"points\":200},{\"id\":4,\"attempts\":2,\"points\":300}]}";
    
      Serial.println(json);
      int httpCode = http1.PUT(json);

      if (httpCode > 0) {
        Serial.printf("[HTTP] PUT... code: %d\n", httpCode);

        if (httpCode == HTTP_CODE_OK) {
          const String& payload = http.getString();
          Serial.println("received payload:\n<<");
          Serial.println(payload);
          Serial.println(">>");
        }
      } else {
        Serial.printf("[HTTP] PUT... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }
      delay(random(100, 300));
      http1.end();
    }
    
    http.end();
  }

  delay(10000);
}

void loop() {
 
}