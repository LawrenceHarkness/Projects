#include <Servo.h>
Servo servo;
void setup() {
  servo.attach(8);
  servo.write(0);
}
void loop() {
  servo.write(0);
  delay(5000);
  servo.write(50);
                        
  delay(200); 
}

  
      
 
