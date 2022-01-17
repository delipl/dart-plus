
#include "access_point.hpp"

AccessPoint::AccessPoint(const String &name, const String &pass):
stassid(name), stapsk(pass){
    Serial.println();
    Serial.println("Creating server...");

    server = std::make_shared<AsyncWebServer>(80);

    Serial.print("Setting AP (Access Point)…");
    WiFi.softAP(stassid, stapsk);
    IPAddress IP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(IP);
    Serial.print("Local ip address: ");
    Serial.println(WiFi.localIP());
    ip = WiFi.softAPIP();

    server->on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
        request->send_P(200, "text/html", (const uint8_t *)FPSTR(index_html), 'e');
    });

    server->begin();
}