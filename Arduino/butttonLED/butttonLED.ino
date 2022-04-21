
#include <Servo.h>
Servo myservo;
Servo myservo8;
const int buttonPin = 2;     
int motorPin = 7;

int pos = 0;
int angle = 0; 
int buttonState = 0;         

void setup() {
  // initialize the LED pin as an output:
 
  // initialize the pushbutton pin as an input:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buttonPin, INPUT);
  myservo.attach(9);
  myservo8.attach(8);
  myservo.write(0);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
    digitalWrite(motorPin, HIGH);

    if (buttonState == HIGH)   
    while (angle <= 120) {
       angle = angle + 1;
       myservo.write(angle);
       
       delay(20);      
      }
    while (angle >= 0) {
       angle = angle - 1;
       myservo.write(angle);
       
       delay(20);      
      }  
     
     
 
    
  }
