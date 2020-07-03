#include <Servo.h>
int ButtonState1;
int ButtonState2;
int ButtonState3;
int ButtonState4;

Servo servo1;

int val;    // variable to read the value from the analog pin
const int ButtonPin1 = 1;
const int ButtonPin2 = 2;
const int ButtonPin3 = 3;
const int ButtonPin4 = 4;

void setup() {
  servo1.attach(7, 0, 360);

  pinMode(ButtonPin1, INPUT);
  pinMode(ButtonPin2, INPUT);
  pinMode(ButtonPin3, INPUT);
  pinMode(ButtonPin4, INPUT);

    servo1.write(0);
    
}
void loop() {
  ButtonState1 = digitalRead(ButtonPin1);
  ButtonState2 = digitalRead(ButtonPin2);
  ButtonState3 = digitalRead(ButtonPin3);
  ButtonState4 = digitalRead(ButtonPin4);
  if (ButtonState1 == HIGH && ButtonState2 == HIGH && ButtonState3 == HIGH && ButtonState4 == HIGH){
  
  servo1.write(90);

  }
  else{ 
  servo1.write(0);
  
  
  
  
  }
  //val = analogRead(0);            // reads the value of the potentiometer (value between 0 and 1023)
  //val = map(val, 0, 1023, 0, 360);     // scale it to use it with the servo (value between 0 and 180)
  //servo1.write(val);
  

}
