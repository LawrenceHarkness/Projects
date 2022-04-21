#include <Servo.h>
Servo left;
Servo right;
int val = 0;
int pos = 0;
int angle = 0; 

void setup() {
   left.attach(9);
   right.attach(8);
   
   left.write(90);
   right.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  left.write(0);
  right.write(180);


}
