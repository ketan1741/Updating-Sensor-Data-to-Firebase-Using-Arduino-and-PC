import pyrebase

config = {
   "apiKey": "AIzaSyA2aLLP-4XMFhiYVGBU_QfUoIjXuNqZurg",
    "authDomain": "iet1-5ddc6.firebaseapp.com",
    "databaseURL": "https://iet1-5ddc6.firebaseio.com",
    "projectId": "iet1-5ddc6",
    "storageBucket": "iet1-5ddc6.appspot.com",
    "messagingSenderId": "819459300721",
    "appId": "1:819459300721:web:73ab2382ecbbb785"
  };

firebase = pyrebase.initialize_app(config)
db = firebase.database()
import serial
import re
try:
    arduino=serial.Serial("COM3",timeout=1)
except:
    print("please check port")
while True:
    a=str(arduino.readline())
    x=re.findall('[0-9]+',a)
    if(len(x)==0):
        v=0
    else:
        v=x[0]
    dist={"Distace":v}
    db.child("Ultrasonic").set(dist)
    print("Distance:",v)

        
