import time
import requests
import RPi.GPIO as GPIO
SEN_PIN = 36 #IR sensor腳位
data = {
    "name": "Jason",
    "SENSOR": "ON"
}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SEN_PIN,GPIO.IN)
try:
    while True:
        #print(GPIO.input(SEN_PIN))
        if GPIO.input(SEN_PIN) == GPIO.HIGH:#有人接進時觸發反應
            r = requests.get('https://4146513691a2.ngrok.io/callback', params=data)
        time.sleep(1)
except Exception as e:
    print(e)
