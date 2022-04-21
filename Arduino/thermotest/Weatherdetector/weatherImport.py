import json
import time as t
import serial
import datetime
import os
#from datetime import datetime #Weathersender78
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl




port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pythonweatherroom@gmail.com"  # Enter your address
receiver_email = "lawrenceharkness3@gmail.com"  # Enter receiver address
password = input("please enter password")
bodymessage = """\
Subject: Hi there

This message is sent from Python."""




serialPort = serial.Serial(port = "COM3", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
weatherList = ""
serialString = ""                           # Used to hold data coming over UART
counter = 0

while(1):


    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        print(serialString.decode('Ascii'))
        weatherList =  serialString.decode('Ascii')
        time = datetime.datetime.now()
        data = json.loads(weatherList)
        line_data = '{},{},{},{}\n'.format(data["Light levels"],data["Temperature"],data["Humidity"],time)

        if data["Temperature"] == -999.00 or  data["Humidity"] == -999.00:
            pass
        else:


            # Tell the device connected over the serial port that we recevied the data!
            # The b at the beginning is used to indicate bytes!
            serialPort.write(b"Thank you for sending data \r\n")
            if not os.path.exists("./weather.csv"):

                with open('weather.csv', 'w') as f:
                    f.write(str("Light,Temperature,Humidity,Timestamp\n"))

            if weatherList != "":

                with open('weather.csv', 'a') as f:
                    f.write(str(line_data))
    t.sleep(1)
    counter = counter + 1

    if counter == 10:
        print("sending email")
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'
        # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(bodymessage, 'plain'))
        attach_file_name = 'weather.csv'
        attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)  # encode the attachment
        # add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        with open('weather.csv', 'w') as f:
            f.write(str("Light,Temperature,Humidity,Timestamp\n"))

