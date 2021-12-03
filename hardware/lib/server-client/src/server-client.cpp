#include "server-client.h"

ServerClient::ServerClient(const String &stassid, const String &stapsk, const String &ipAddress):
stassid{stassid}, stapsk{stapsk}, ipAddress{ipAddress}
{
    WiFi.begin(stassid, stapsk);
    Serial.println("Connectiong to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        
    }
    Serial.println("");
    Serial.print("Connected! IP address: ");
    Serial.println(WiFi.localIP());

}

RequestError ServerClient::SendSettings(StaticJsonDocument<SIZE_SETTINGS_JSON> doc){
    if ((WiFi.status() == WL_CONNECTED)) {
            WiFiClient client;
            HTTPClient http;
            http.begin(client, this->ipAddress); 
            http.addHeader("Content-Type", "application/json");

            Serial.print("[HTTP] POST...\n");
            String json;
            serializeJson(doc, json);
            // serializeJsonPretty(doc, Serial);
            int httpCode = http.POST(json);
            
            if (httpCode > 0) {
                Serial.printf("[HTTP] POST... code: %d\n", httpCode);

                if (httpCode == HTTP_CODE_OK) {
                    const String& payload = http.getString();
                    Serial.println("received payload:\n<<");
                    Serial.println(payload);
                    Serial.println(">>");
                    return RequestError_OK;
                }
            } 
            else {
                Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
            }
        }
    return RequestError_Error;
}


RequestError ServerClient::SendGame(StaticJsonDocument<SIZE_GAME_JSON> doc){
    if ((WiFi.status() == WL_CONNECTED)) {
            WiFiClient client;
            HTTPClient http;
            http.begin(client, this->ipAddress); 
            http.addHeader("Content-Type", "application/json");

            Serial.print("[HTTP] PUT...\n");
            String json;
            serializeJson(doc, json);
            // serializeJsonPretty(doc, Serial);
            int httpCode = http.PUT(json);
            
            if (httpCode > 0) {
                Serial.printf("[HTTP] PUT... code: %d\n", httpCode);

                if (httpCode == HTTP_CODE_OK) {
                    const String& payload = http.getString();
                    Serial.println("received payload:\n<<");
                    Serial.println(payload);
                    Serial.println(">>");
                    return RequestError_OK;
                }
            } 
            else {
                Serial.printf("[HTTP] PUT... failed, error: %s\n", http.errorToString(httpCode).c_str());
            }
        }
    return RequestError_Error;
}