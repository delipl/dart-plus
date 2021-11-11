#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define SERVER_IP "http://192.168.192.3:8000/settings/add"

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

}

void loop() {
  // wait for WiFi connection
  if ((WiFi.status() == WL_CONNECTED)) {

    WiFiClient client;
    HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    http.begin(client, SERVER_IP); 
    http.addHeader("Content-Type", "application/json");

    Serial.print("[HTTP] POST...\n");
    // uint8_t jsonValues[108] = "{\"gameStatus\":1,\"maxThrow\":132,\"numberOfThrow\":12,\"round\":0,\"throwingPlayerId\":33}";
    // Serial.println((char*)jsonValues);
    int httpCode = http.POST("{\"gameStatus\":1,\"maxThrow\":132,\"numberOfThrow\":12,\"round\":0,\"throwingPlayerId\":33}");

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

    http.end();
  }

  delay(10000);
}