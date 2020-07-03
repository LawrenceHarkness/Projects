 
#include <Adafruit_SoftServo.h>  // SoftwareServo (works on non PWM pins)
 
#define SERVO1PIN 9   // Servo control line (orange) on Trinket Pin #0
 

Adafruit_SoftServo myServo1, myServo2;  //create TWO servo objects
   
void setup() {
  // Set up the interrupt that will refresh the servo for us automagically
  OCR0A = 0xAF;            // any number is OK
  TIMSK |= _BV(OCIE0A);    // Turn on the compare interrupt (below!)
  
  myServo1.attach(SERVO1PIN);   // Attach the servo to pin 0 on Trinket
  myServo1.write(90);           // Tell servo to go to position per quirk
  delay(15);                    // Wait 15ms for the servo to reach the position
}
 
void loop()  {
  myServo1.write(90);                    // tell servo to go to position
 
  delay(15);                              // waits 15ms for the servo to reach the position
   myServo1.write(180);                    // tell servo to go to position
 
  delay(15);        
}
 
// We'll take advantage of the built in millis() timer that goes off
// to keep track of time, and refresh the servo every 20 milliseconds
// The SIGNAL(TIMER0_COMPA_vect) function is the interrupt that will be
// Called by the microcontroller every 2 milliseconds
volatile uint8_t counter = 0;
SIGNAL(TIMER0_COMPA_vect) {
  // this gets called every 2 milliseconds
  counter += 2;
  // every 20 milliseconds, refresh the servos!
  if (counter >= 20) {
    counter = 0;
    myServo1.refresh();
  }
}
