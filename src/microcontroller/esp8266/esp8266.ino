// Neopixel
#include <Adafruit_NeoPixel.h>

// ESP8266
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

// Internal Webserver Config
const char *ssid = "<<SSID>>";
const char *password = "<<SSID_PASSWORD>>";
ESP8266WebServer server ( 80 );

// External Webserver Config
const char *external_server = "<<external server>>";

// LED Strips Config
#define LOWER_LEFT_PIN D2
#define LOWER_RIGHT_PIN D4
#define UPPER_LEFT_PIN D5
#define UPPER_RIGHT_PIN D6
#define NUM_LEDS 16
#define NUM_STRIPS 4

// LED Strips
Adafruit_NeoPixel LOWER_LEFT_STRIP = Adafruit_NeoPixel(NUM_LEDS, LOWER_LEFT_PIN, NEO_RGB + NEO_KHZ800);
Adafruit_NeoPixel LOWER_RIGHT_STRIP = Adafruit_NeoPixel(NUM_LEDS, LOWER_RIGHT_PIN, NEO_RGB + NEO_KHZ800);
Adafruit_NeoPixel UPPER_LEFT_STRIP = Adafruit_NeoPixel(NUM_LEDS, UPPER_LEFT_PIN, NEO_RGB + NEO_KHZ800);
Adafruit_NeoPixel UPPER_RIGHT_STRIP = Adafruit_NeoPixel(NUM_LEDS, UPPER_RIGHT_PIN, NEO_RGB + NEO_KHZ800);
Adafruit_NeoPixel strips[NUM_STRIPS] = { LOWER_LEFT_STRIP, LOWER_RIGHT_STRIP, UPPER_LEFT_STRIP, UPPER_RIGHT_STRIP };

const int led = 13;

// -------------------------
// -------------------------
// --------- ROUTER --------
// -------------------------
// -------------------------

// Route = "/healthcheck"
void healthcheck(){
  DynamicJsonDocument doc(2048);
  doc["status"] = 200;
  doc["health"] = "healthy";
  
  // Serialize JSON document
  String json;
  serializeJson(doc, json);
  
  server.send( 200, "application/json", json);
}

// Route = "/updateLEDs"
void updateLEDs(){
  String param = server.arg(0);
  
  DynamicJsonDocument doc(2048);
  DeserializationError error = deserializeJson(doc, param);

  JsonObject postObj = doc.as<JsonObject>();

  // TODO: Logic.

  Serial.println("Updated LED colors");

  replyWith200OK();
}


// -------------------------
// -------------------------
// --- HELPER FUNCTIONS ---
// -------------------------
// -------------------------

void replyWith200OK(){
  DynamicJsonDocument doc(2048);
  doc["status"] = "OK";
  
  // Serialize JSON document
  String json;
  serializeJson(doc, json);
  
  server.send( 200, "application/json", json);
}

void setLEDColor(int r, int g, int b, String stripLocation, int ledID){
  if(stripLocation == "ALL")
    for(int i = 0; i < NUM_STRIPS; i++)
      strips[i].setPixelColor(ledID, strips[i].Color( g, r, b ));
  else
    if(stripLocation.equals("LOWER_LEFT"))
        LOWER_LEFT_STRIP.setPixelColor(ledID, LOWER_LEFT_STRIP.Color( g, r, b));
    else if(stripLocation.equals("LOWER_RIGHT"))
        LOWER_RIGHT_STRIP.setPixelColor(ledID, LOWER_RIGHT_STRIP.Color( g, r, b));
    else if(stripLocation.equals("UPPER_LEFT"))
        UPPER_LEFT_STRIP.setPixelColor(ledID, UPPER_LEFT_STRIP.Color( g, r, b));
    else if(stripLocation.equals("UPPER_RIGHT"))
        UPPER_RIGHT_STRIP.setPixelColor(ledID, UPPER_RIGHT_STRIP.Color( g, r, b));

  // Show colors:
  for(int i = 0; i < NUM_STRIPS; i++)
    strips[i].show();
}

void setStripColor(int r, int g, int b, int brightness, String stripLocation){
  if(stripLocation == "ALL")
    for(int i = 0; i < NUM_STRIPS; i++){
      strips[i].setBrightness(brightness);
      for(int j=0; j < NUM_LEDS; j++)
        strips[i].setPixelColor(j, strips[i].Color( g, r, b ) );
    }
  else
    if(stripLocation.equals("LOWER_LEFT")){
        LOWER_LEFT_STRIP.setBrightness(brightness);
        for(int i = 0; i < NUM_LEDS; i++)
          LOWER_LEFT_STRIP.setPixelColor(i, LOWER_LEFT_STRIP.Color( g, r, b));
    }
    else if(stripLocation.equals("LOWER_RIGHT")){
        LOWER_RIGHT_STRIP.setBrightness(brightness);
        for(int i = 0; i < NUM_LEDS; i++)
          LOWER_RIGHT_STRIP.setPixelColor(i, LOWER_RIGHT_STRIP.Color( g, r, b));
    }
    else if(stripLocation.equals("UPPER_LEFT")){
        UPPER_LEFT_STRIP.setBrightness(brightness);
        for(int i = 0; i < NUM_LEDS; i++)
          UPPER_LEFT_STRIP.setPixelColor(i, UPPER_LEFT_STRIP.Color( g, r, b));
    }
    else if(stripLocation.equals("UPPER_RIGHT")){
        UPPER_RIGHT_STRIP.setBrightness(brightness);
        for(int i = 0; i < NUM_LEDS; i++)
          UPPER_RIGHT_STRIP.setPixelColor(i, UPPER_RIGHT_STRIP.Color( g, r, b));
    }
  
  // Show colors:
  for(int i = 0; i < NUM_STRIPS; i++)
    strips[i].show();
}

// -------------------------
// -------------------------
// - CENTRAL SERVER COMMS --
// -------------------------
// -------------------------

void register_device(){ 
  HTTPClient http;
  WiFiClient client;

  DynamicJsonDocument doc(2048);
  doc["MAC_Address"] = WiFi.macAddress();
  doc["IP_Address"] = WiFi.localIP();
  
  // Serialize JSON document
  String json;
  serializeJson(doc, json);
  
  // Send request
  http.useHTTP10(true);
  http.begin(client, external_server + "/register");
  http.POST(json);
  
  // Disconnect
  http.end();
}

// -------------------------
// -------------------------
//  - ESP8266 MAIN METHODS -
// -------------------------
// -------------------------

void setup ( void ) {
  Serial.begin ( 115200 );

  // NeoPixel start
  Serial.println();
  for(int i = 0; i < NUM_STRIPS; i++){
    strips[i].begin();
    strips[i].setBrightness(0);
    for(int j = 0; j < NUM_LEDS; j++)
      strips[i].setPixelColor(j, strips[i].Color( 0, 0, 0));
    strips[i].show();
  }
  
  // Webserver
  pinMode ( led, OUTPUT );
  digitalWrite ( led, 0 );
  
  WiFi.begin ( ssid, password );
  Serial.println ( "" );

  // Wait for connection
  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  Serial.println ( "" );
  Serial.print ( "Connected to " );
  Serial.println ( ssid );
  Serial.print ( "IP address: " );
  Serial.println ( WiFi.localIP() );

  if ( MDNS.begin ( "esp8266" ) ) {
    Serial.println ( "MDNS responder started" );
  }

  // what to do with requests
  server.on ( "/healthcheck", HTTP_GET, healthcheck );
  server.on ( "/updateLEDs", HTTP_POST, updateLEDs );
  server.begin();
  
  Serial.println ( "HTTP server started" );
  
  register_device();
}

void loop ( void ) {
  // waiting for a client
  server.handleClient();
}
