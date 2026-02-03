#include <M5StickCPlus2.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// Replace with your Wi-Fi credentials
const char* ssid     = "Aryan's Hotspot";
const char* password = "aryan2005";

// JokeAPI endpoint
const char* jokeApiUrl = "https://v2.jokeapi.dev/joke/Any";

// Function to connect to Wi-Fi
void connectToWiFi() {
  M5.Lcd.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    M5.Lcd.print(".");
  }

  M5.Lcd.println();
  M5.Lcd.println("Connected to Wi-Fi");
}

// Function to fetch a random joke
String getRandomJoke() {
  if ((WiFi.status() == WL_CONNECTED)) {
    HTTPClient http;
    http.begin(jokeApiUrl);
    
    int httpResponseCode = http.GET();
    
    if (httpResponseCode > 0) {
      String payload = http.getString();
      
      // Parse JSON
      StaticJsonDocument<1024> doc;
      deserializeJson(doc, payload);

      String joke;
      if (doc["type"] == "single") {
        joke = doc["joke"].as<String>();
      } else {
        joke = doc["setup"].as<String>() + "\n" + doc["delivery"].as<String>();
      }
      
      http.end();
      return joke;
    } else {
      http.end();
      return "Failed to retrieve joke.";
    }
  } else {
    return "Not connected to Wi-Fi.";
  }
}

void setup() {
  M5.begin();
  M5.Lcd.setRotation(0);  // Set screen orientation
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setTextColor(WHITE);
  M5.Lcd.setTextSize(1);

  connectToWiFi();

  M5.Lcd.clear();
  M5.Lcd.setCursor(0, 0);
  String joke = getRandomJoke();
  M5.Lcd.println(joke);
}

void loop() {
  if (M5.BtnA.wasPressed()) {
    M5.Lcd.clear();
    M5.Lcd.setCursor(0, 0);
    String joke = getRandomJoke();
    M5.Lcd.println(joke);
  }

  // Check if Button B is pressed
  if (M5.BtnB.wasPressed()) {
    M5.Lcd.clear();
    M5.Lcd.setCursor(0, 0);
    M5.Lcd.println("Press A for a new joke!");
  }

  M5.update();
}
