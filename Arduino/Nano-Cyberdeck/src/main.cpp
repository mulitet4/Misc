#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>

// Define pin connections for the ESP32
#define PIN_RST  25  // Reset
#define PIN_DC   26  // Data/Command
#define PIN_CS   27  // Chip Select
#define PIN_SCK  18  // SPI Clock
#define PIN_MOSI 23  // SPI MOSI

// SSD1309 Commands
#define SSD1309_SET_COLUMN_ADDR  0x21
#define SSD1309_SET_PAGE_ADDR    0x22
#define SSD1309_SET_CONTRAST     0x81
#define SSD1309_DISPLAY_ON       0xAF
#define SSD1309_DISPLAY_OFF      0xAE
#define SSD1309_SET_DISPLAY_START_LINE 0x40

// Function to send a command to the display
void sendCommand(uint8_t cmd) {
  digitalWrite(PIN_DC, LOW);  // DC low for command
  digitalWrite(PIN_CS, LOW);  // Activate chip
  SPI.transfer(cmd);          // Send the command
  digitalWrite(PIN_CS, HIGH); // Deactivate chip
}

// Function to send data to the display
void sendData(uint8_t data) {
  digitalWrite(PIN_DC, HIGH); // DC high for data
  digitalWrite(PIN_CS, LOW);  // Activate chip
  SPI.transfer(data);         // Send the data
  digitalWrite(PIN_CS, HIGH); // Deactivate chip
}

// Function to initialize the display
void initDisplay() {
  // Reset the display
  digitalWrite(PIN_RST, LOW);
  delay(10);
  digitalWrite(PIN_RST, HIGH);
  delay(10);

  // Initialization sequence for SSD1309
  sendCommand(SSD1309_DISPLAY_OFF);
  sendCommand(SSD1309_SET_CONTRAST);
  sendCommand(0x7F);  // Set contrast to mid-level (could be adjusted)

  sendCommand(SSD1309_SET_DISPLAY_START_LINE);  // Set start line

  sendCommand(SSD1309_SET_COLUMN_ADDR);
  sendCommand(0);    // Start column address
  sendCommand(127);  // End column address (for 128x32 display)

  sendCommand(SSD1309_SET_PAGE_ADDR);
  sendCommand(0);    // Start page address
  sendCommand(3);    // End page address (for 32 pages on 128x32 display)

  sendCommand(SSD1309_DISPLAY_ON);  // Turn on the display
}

// Function to plot a pixel at (x, y)
void plotPixel(uint8_t x, uint8_t y) {
  // Set the column and page address
  sendCommand(SSD1309_SET_COLUMN_ADDR);
  sendCommand(x);     // Column start
  sendCommand(x);     // Column end (for single pixel)

  sendCommand(SSD1309_SET_PAGE_ADDR);
  sendCommand(y / 8); // Page (byte) address
  sendCommand(y / 8); // Same page

  // Send data to set the pixel. Each page is 8 pixels tall.
  uint8_t data = (1 << (y % 8));  // Set the bit corresponding to the pixel's position
  sendData(data);  // Set the pixel at (x, y)
}

void setup() {
  // Set pin modes
  pinMode(PIN_CS, OUTPUT);
  pinMode(PIN_RST, OUTPUT);
  pinMode(PIN_DC, OUTPUT);

  // Initialize SPI
  SPI.begin(PIN_SCK, -1, PIN_MOSI, -1);
  SPI.beginTransaction(SPISettings(10000000, MSBFIRST, SPI_MODE0)); // 10MHz speed

  // Initialize display
  initDisplay();

  // Plot a pixel at position (x=10, y=10)
  plotPixel(10, 10);
}

void loop() {
  // Nothing to do here in this rudimentary example
}
