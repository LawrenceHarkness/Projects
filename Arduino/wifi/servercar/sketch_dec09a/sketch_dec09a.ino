
/*********************
ESP8266 as a TCP Servicer
*********************/


#define DEBUG true
#define SSID "SKYE186E"  // your ssid
#define PASS "DYAPAQSY" //pass word

// Emulate Serial1 on pins 6/7 if not present
#ifndef HAVE_HWSERIAL1
#include "SoftwareSerial.h"
SoftwareSerial Serial1(2, 3); // RX, TX
#endif

void setup()
{
  Serial.begin(9600);
  Serial1.begin(9600); // your esp's baud rate might be different
 
  sendData("AT+CWMODE=3\r\n",1000,DEBUG); // configure as access point 
  sendData("AT+RST\r\n",2000,DEBUG); // reset module
 
       //connect to the wifi
       boolean connected=false;
       for(int i=0;i<5;i++)
       {
           if(connectWiFi())
           {
               connected = true;
                   break;
             }
         }
/*         if (!connected){while(1);}
         delay(3000); */
  sendData("AT+CIFSR\r\n",1000,DEBUG);// get ip address
  sendData("AT+CIPMUX=1\r\n",1000,DEBUG); // configure for multiple connections
  sendData("AT+CIPSERVER=1,80\r\n",1000,DEBUG); // turn on server on port 80
}
 
void loop()
{
  if(Serial1.available()) // check if the esp is sending a message 
  {
//    
//    while(Serial.available())
//    {
//      // The esp has data so display its output to the serial window 
//      char c = Serial.read(); // read the next character.
//      sofSerial.write(c);
//    } 
//
    if(Serial1.find("+IPD,"))
    {
     delay(1000);
 
     int connectionId = Serial1.read()-48; // subtract 48 because the read() function returns 
                                           // the ASCII decimal value and 0 (the first decimal number) starts at 48
     
     String webpage = "<h1>Hello</h1>";
 
     String cipSend = "AT+CIPSEND=";
     cipSend += connectionId;
     cipSend += ",";
     cipSend +=webpage.length();
     cipSend +="\r\n";
     
     sendData(cipSend,1000,DEBUG);
     sendData(webpage,1000,DEBUG);

     String closeCommand = "AT+CIPCLOSE="; 
     closeCommand+=5;
     closeCommand+="\r\n";
     sendData(closeCommand,3000,DEBUG);
     sendData("AT+RESTORE\r\n",3000,DEBUG);
    }
  }
}
 
 
String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    
    Serial1.print(command); // send the read character to the Serial
    
    long int time = millis();
    
    while( (time+timeout) > millis())
    {
      while(Serial1.available())
      {
        
        // The esp has data so display its output to the serial window 
        char c = Serial1.read(); // read the next character.
        response+=c;
      }  
    }
    
    if(debug)
    {
      Serial.print(response);
    }
    
    return response;
}

boolean connectWiFi()
{
       String cmd="AT+CWJAP=\"";
       cmd+=SSID;
       cmd+="\",\"";
       cmd+=PASS;
       cmd+="\"";
       Serial1.println(cmd);
       Serial1.println(cmd);
       delay(5000);
       if(Serial1.find("OK"))
     {
          Serial.println("OK, Connected to WiFi.");
     return true;
     }else
     {
           Serial.println("Can not connect to the WiFi.");
           return false;
     }
}
