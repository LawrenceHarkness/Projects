// for 360 servo white to yellow blue to red purple to brown
// 

#include <Servo.h>
Servo steer;
Servo drive;
const int right = 12;
const int left = 11;
const int forward = 10;
const int back = 9;
int SlidingSteer = A4;
int val = 0;
int pos = 0;
int angle = 0; 
int rightState = 0;
int leftState = 0;   
int forwardState = 0;
int backwardState=0;

void setup() {
  // put your setup code here, to run once:
  
  drive.attach(6);
  drive.write(90);
  steer.attach(5);
  steer.write(0);
  pinMode(forward, INPUT);
  pinMode(back, INPUT);
  
  pinMode(right, INPUT);
  pinMode(left, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
   rightState = digitalRead(right);
   leftState = digitalRead(left);
   forwardState = digitalRead(forward);
   backwardState= digitalRead(back);
   val = analogRead(SlidingSteer);
   
  
  if (forwardState == LOW){
  drive.write(180);

  }
  
  else if (backwardState == LOW){
  drive.write(0); 
  }
  else {
  drive.write(90);
  }
   


  int steerAngle = (int)(val *0.18);
  steer.write(steerAngle); 
   
  /*if (rightState == LOW){ //button steering
  steer.write(180);

  }
  
  else if (leftState == LOW){
  steer.write(0); // future me remmber blue servo is 180dg wheras grey lego one is 270dg
  }
  else {
  steer.write(90);
  }
  */
  
  }
 

  
  
 
   

   
