#include "DHT.h"
int photocellPin = 0;
int photocellReading;

dht DHT;

#define DHT11_PIN 7

void setup(){
  Serial.begin(9600);
}

void loop(){
  int chk = DHT.read11(DHT11_PIN);
  photocellReading = analogRead(photocellPin);
  Serial.print("{\"Light levels\":");
  Serial.print(photocellReading);
  Serial.print( ",\"Temperature\":");
  Serial.print(DHT.temperature);
  Serial.print( ",\"Humidity\":");
  Serial.print(DHT.humidity);
  Serial.println("}");
  delay(1000);
}
