
#include <Servo.h>
Servo servo;
const int ledPin =  13;      // the number of the LED pin
const int buttonPin = 2; 
// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  servo.attach(8);
  pinMode(buttonPin, INPUT);
  servo.write(0);
}
void loop() {
  
  buttonState = digitalRead(buttonPin);

  
  if (buttonState == HIGH) {
      
    servo.write(180);
  } else {
   
    servo.write(0);                  
  }
