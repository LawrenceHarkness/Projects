// set up for temperature sensor 
#include "DHT.h"
dht DHT;
#define DHT11_PIN 7
#include <Servo.h>

// set up for servos 
Servo SWon;
Servo SWoff;
#define servoPinOn 10
#define servoPinOff 9
int angle = 0;


void setup(){
  // in moniter set baudrate to 9600 
  Serial.begin(9600);
  // ataching the servos 
  SWon.attach(servoPinOn);
  SWoff.attach(servoPinOff);
}

void loop(){
  
  // sorting the -999 temperature reads out 
  int chk = DHT.read11(DHT11_PIN);
  if (DHT.temperature == -999) {
  }
  
  
  else {
    
    // sets Desired Temperature (DT) to the sensors reads and prints output to moniter 
    int DT = DHT.temperature; 
    Serial.print(DT);
    Serial.println("}");
  delay(1000);
  
  // checks the if desired temperature is 18 degrees if so tells the servos to switch the switch off
  // SWITCH OFF
   
  if (DT >= 20){
    SWon.write(0);
    delay(1000);
    SWoff.write(50);
    Serial.print("Heater Off ");
 // if the temperature is not 24 degrees it  will switch the switch back on 
 // SWITCH ON
 }else{
  SWoff.write(180);
  delay(1000);
  SWon.write(30);
  Serial.print("Heater On ");
  }
 }
      

  }
 
  
  
