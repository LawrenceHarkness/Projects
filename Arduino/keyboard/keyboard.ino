#include "pitches.h"  //add note library
int ButtonState1;
int ButtonState2;
int ButtonState3;
int ButtonState4;

int melody1[]={NOTE_B0,};
int melody2[]={NOTE_A3,};
int melody3[]={NOTE_G3,};
int melody4[]={NOTE_DS8,};
int val; 

const int ButtonPin1 = 6;
const int ButtonPin2 = 5;
const int ButtonPin3 = 4;
const int ButtonPin4 = 3;

void setup(){ 
  pinMode(ButtonPin1, INPUT);
  pinMode(ButtonPin2, INPUT);
  pinMode(ButtonPin3, INPUT);
  pinMode(ButtonPin4, INPUT);

}
void loop(){
  //read the input pin
  ButtonState1 = digitalRead(ButtonPin1);
  ButtonState2 = digitalRead(ButtonPin2);
  ButtonState3 = digitalRead(ButtonPin3);
  ButtonState4 = digitalRead(ButtonPin4);
  
  //if the button is pressed
  if (ButtonState1   == HIGH){      
     
      tone(8,melody1);
      delay(250);      
      noTone(8);
  }
  if (ButtonState2 == HIGH){      
     
      tone(8,melody2);
      delay(250);      
      noTone(8);
 
  }
  if (ButtonState3 == HIGH){      
     
      tone(8,melody3);
      delay(250);      
      noTone(8);
 
  }
if (ButtonState4 == HIGH){      
     
      tone(8,melody4);
      delay(250);      
      noTone(8);
 
  }





    
    
    }

    
  
