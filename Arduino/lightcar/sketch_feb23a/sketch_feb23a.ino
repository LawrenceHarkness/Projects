#include <Servo.h>
Servo left;
Servo right;
int val = 0;
int pos = 0;
int angle = 0; 
int photocellPin1 = 0;
int photocellPin2 = 1;
int photocellReading1;
int photocellReading2;




void setup(){
  Serial.begin(9600);
  left.attach(9);
   right.attach(8);
   
   left.write(90);
   right.write(90);
}

void loop(){
  
  photocellReading1 = analogRead(photocellPin1);
  photocellReading2 = analogRead(photocellPin2);
  Serial.print("{\"Light levels for sensor 1\":");
  Serial.println(photocellReading1); 
  Serial.print("{\"Light levels for sensor 2\":");
  Serial.println(photocellReading2);


  
  
  
   if (photocellReading2 > photocellReading1 + 50) {
    left.write(180);
    right.write(180);
    delay(500);
    
  
  }
    else if (photocellReading1 > photocellReading2 + 50) {
    left.write(0);
    right.write(0);
    delay(500);
    
  
}
  else{
  left.write(0);
  right.write(180);

  }

  }
  
  
  
