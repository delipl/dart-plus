/**
 * @file access_point.hpp
 * @author Jakub Delicat (delicat.kuba@gmail.com)
 * @brief File describes class
 * @version 0.1
 * @date 2022-01-16
 *
 * @copyright Copyright (c) 2022
 *
 */
#pragma once
#include <Arduino.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncWebServer.h>
#include <pgmspace.h>

#include <memory>

#include "index.html"

class AccessPoint {
   protected:
    const String stassid;
    const String stapsk;
    IPAddress ip;
    std::shared_ptr<AsyncWebServer> server;



   public:
    AccessPoint(const String &name, const String &pass);
};