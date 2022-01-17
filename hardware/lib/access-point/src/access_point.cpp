
#include "access_point.hpp"

AccessPoint::AccessPoint(const String &name, const String &pass):
stassid(name), stapsk(pass){
    int n = WiFi.scanNetworks();
    Serial.println();
    Serial.print(n);
    Serial.println(" network(s) found:");
    for (int i = 0; i < n; ++i) {
        Serial.print("\t");
        Serial.println(WiFi.SSID(i));
        ssid_list.push_back(WiFi.SSID(i));
    }

    Serial.print("Setting AP (Access Point)…");
    WiFi.softAP(stassid, stapsk);

    Serial.println();
    Serial.println("Creating server...");
    server = std::make_shared<AsyncWebServer>(80);

    IPAddress IP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(IP);

    server->on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
        request->send_P(200, "text/html", index_html, processor_callback);
    });

    connect_to_wifi();
    server->begin();
}

String AccessPoint::processor_callback(const String &var) {
    if(var == "WIFILIST"){
        String buttons;
        for (const auto &ssid : ssid_list) {
            buttons += "<p><button type=\"button\" onclick=\"chooseWifi(this.innerHTML)\">" + ssid + "</button></p>";
        }
        return buttons;
    }
    return "There is no available wifi.";
}

void AccessPoint::connect_to_wifi(){
    server->on("/connect", HTTP_GET, [](AsyncWebServerRequest *request) {
        String wifi_ssid;
        String wifi_psk;
        // GET input1 value on <ESP_IP>/update?output=<inputMessage1>&state=<inputMessage2>
        if (request->hasParam("ssid") && request->hasParam("psk")) {
            wifi_ssid = request->getParam("ssid")->value();
            wifi_psk = request->getParam("psk")->value();
        } else {
            wifi_ssid = "No message sent";
            wifi_psk = "No message sent";
        }
        Serial.print("SSID: ");
        Serial.print(wifi_ssid);
        Serial.print("\tPSK: ");
        Serial.println(wifi_psk);
        request->send(200, "text/plain", "OK");
    });
}