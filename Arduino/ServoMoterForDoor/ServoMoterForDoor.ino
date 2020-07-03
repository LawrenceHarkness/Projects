#include <Servo.h>

Servo servo1;
int val;    // variable to read the value from the analog pin

void setup() {
  servo1.attach(7, 0, 180);

  
  
}
void loop() {
    
  val = analogRead(0);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 360);     // scale it to use it with the servo (value between 0 and 180)
  servo1.write(val);
  

}

  
  
     
