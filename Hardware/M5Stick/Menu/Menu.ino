#include <M5StickCPlus2.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// Replace with your Wi-Fi credentials
const char* ssid     = "Aryan's Hotspot";
const char* password = "aryan2005";

// Menu items
const char* menuItems[] = {"Get Joke", "Weather", "Option 3", "Option 4"};
int menuLength = sizeof(menuItems) / sizeof(menuItems[0]);
int currentSelection = 0;

// JokeAPI endpoint
const char* jokeApiUrl = "https://v2.jokeapi.dev/joke/Any";
const char* weatherUrl = "https://api.open-meteo.com/v1/forecast?latitude=13.35&longitude=74.7833&hourly=temperature_2m,relative_humidity_2m,rain,showers&timezone=Asia%2FTokyo&forecast_days=1";

void scrollText(const String& text, int delayMs) {
  int textWidth = M5.Lcd.textWidth(text);
  int screenWidth = M5.Lcd.width();
  
  for (int x = screenWidth; x > -textWidth; x--) {
    M5.Lcd.fillScreen(BLACK); // Clear the screen
    M5.Lcd.setTextColor(WHITE); // Set text color
    M5.Lcd.setCursor(x, M5.Lcd.height() / 2); // Set the starting position
    M5.Lcd.print(text); // Print the text
    delay(delayMs); // Pause for a moment
  }
}


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
  if (WiFi.status() == WL_CONNECTED) {
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

String padLeft(int number, int width) {
  String str = String(number);
  while (str.length() < width) {
      str = "0" + str;
  }
  return str;
}

String getWeatherForecast(){
  if(WiFi.status() != WL_CONNECTED){
    return "Not connected to Wi-Fi.";
  }

  HTTPClient http;
  http.begin(weatherUrl);
  int httpResponseCode = http.GET();
  
  if (httpResponseCode <= 0){
    return "Failed to retrieve joke.";
  }
    
  String payload = http.getString();
  StaticJsonDocument<1024> doc;
  deserializeJson(doc, payload);

  String weather = "";
  float total_temp = 0;       // Initialize to 0
  int total_humidity = 0;   // Initialize to 0
  float total_showers = 0;    // Initialize to 0
  float total_rain = 0;    // Initialize to 0

  weather += "i  Temp   Humid  Shwrs  Rain\n";

  JsonArray tempArray = doc["hourly"]["temperature_2m"].as<JsonArray>();
  int length = tempArray.size();
  
  for(int i = 9; i < length; i++){
    weather += padLeft(i, 2) + " " + String(doc["hourly"]["temperature_2m"][i].as<float>()) +  "  " + doc["hourly"]["relative_humidity_2m"][i].as<String>() + "     " + String(doc["hourly"]["showers"][i].as<float>()) + "   " + doc["hourly"]["rain"][i].as<String>() + "\n";
    // total_temp += doc["hourly"]["temperature_2m"][i].as<float>();
    // total_humidity += doc["hourly"]["relative_humidity_2m"][i].as<int>();
    // total_rain += doc["hourly"]["rain"][i].as<float>();
    // total_showers += doc["hourly"]["showers"][i].as<float>();
  }

  // float avg_temp = total_temp / (float)length;
  // float avg_humid = total_humidity / (float)length;
  // float avg_showers = total_showers / (float)length;
  // float avg_rain = total_rain / (float)length;
  return weather;
}

// Function to display the menu
void displayMenu() {
  M5.Lcd.clear();
  M5.Lcd.setCursor(0, 0);
  
  for (int i = 0; i < menuLength; i++) {
    if (i == currentSelection) {
      M5.Lcd.setTextColor(BLUE);  // Highlight selected item
      M5.Lcd.println("> " + String(menuItems[i]));
    } else {
      M5.Lcd.setTextColor(WHITE);  // Regular text for other items
      M5.Lcd.println("  " + String(menuItems[i]));
    }
  }
}

// Function to handle menu selection
void handleSelection() {
  String joke;
  String weather;

  switch (currentSelection) {
    // Get Joke
    case 0:
      if (WiFi.status() != WL_CONNECTED){
        connectToWiFi();
      }
      M5.Lcd.clear();
      M5.Lcd.setCursor(0, 0);
      joke = getRandomJoke();
      M5.Lcd.println(joke);

      while (true) {
        M5.update();
        if (M5.BtnA.wasPressed() || M5.BtnB.wasPressed()) {
          break;  // Exit loop if any button is pressed
        }
        delay(100);  // Small delay to avoid tight looping
      }
      break;

    case 1:
      if (WiFi.status() != WL_CONNECTED){
        connectToWiFi();
      }
      M5.Lcd.clear();
      M5.Lcd.setCursor(0, 0);
      weather = getWeatherForecast();
      M5.Lcd.println(weather);

      while (true) {
        M5.update();
        if (M5.BtnA.wasPressed() || M5.BtnB.wasPressed()) {
          break;  // Exit loop if any button is pressed
        }
        delay(100);  // Small delay to avoid tight looping
      }
      break;

    case 2:
      M5.Lcd.clear();
      M5.Lcd.println("Option 3 selected");
      break;
    
    case 3:
      M5.Lcd.clear();
      M5.Lcd.println("Option 4 selected");
      break;
    
    default:
      break;
  }
  
  displayMenu();  // Return to the menu
}

void setup() {
  M5.begin();
  M5.Lcd.setRotation(1);  // Set screen orientation
  M5.Lcd.fillScreen(BLACK);
  M5.Lcd.setTextColor(WHITE);
  M5.Lcd.setTextSize(1);

  displayMenu();
}

void loop() {
  M5.update();  // Update button states
  
  if (M5.BtnB.wasPressed()) {
    currentSelection--;
    if (currentSelection < 0) {
      currentSelection = menuLength - 1;  // Loop back to the last item
    }
    displayMenu();
  }
  
  if (M5.BtnPWR.wasPressed()) {
    currentSelection++;
    if (currentSelection >= menuLength) {
      currentSelection = 0;  // Loop back to the first item
    }
    displayMenu();
  }

  if (M5.BtnA.wasPressed()) {
    handleSelection();  // Select the current menu item
  }
}