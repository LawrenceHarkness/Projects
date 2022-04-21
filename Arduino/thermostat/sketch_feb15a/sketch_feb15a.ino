
#include <Servo.h>
const int buttonPin = 2; 
Servo myservo2;
Servo myservo;
#define servoPin2 10
#define servoPin 9
int buttonState = 0;
int angle = 0;
void setup() {
  pinMode(buttonPin, INPUT);
  myservo2.attach(servoPin2);
  myservo.attach(servoPin);
}
void loop() {
  buttonState = digitalRead(buttonPin);
  
  if (buttonState == LOW) {
    myservo2.write(0);
    delay(1000);
    myservo.write(50);
  } else {
    myservo.write(180);
  delay(1000);
  myservo2.write(30);
  }
  
  
  


 
  
  
}
