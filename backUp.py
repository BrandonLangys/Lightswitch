import RPi.GPIO as IO
import time
import requests
import pigpio
pi = pigpio.pi() #connects to local pi
from urllib.request import urlopen
pi.set_mode(19, pigpio.OUTPUT)

def turnOn(): # method for turning on
        pi.set_servo_pulsewidth(19,0)
        pi.set_servo_pulsewidth(19,1500)
        print('1500')
        time.sleep(1)
        pi.set_servo_pulsewidth(19,1925)
        print('1925')
        time.sleep(1)
        pi.set_servo_pulsewidth(19,1500)
        print('1500')
        print("Turn light on code here")

def turnOff(): # method for turning off
        pi.set_servo_pulsewidth(19,0)
        pi.set_servo_pulsewidth(19,1500)
        print('1500')
        time.sleep(1)
        pi.set_servo_pulsewidth(19,1200)
        print('1200')
        time.sleep(1)
        pi.set_servo_pulsewidth(19,1500)
        print('1500')
        print("Turn Light OFF Muther!")


def getNum(): # gets the input from the website
         result = requests.get("")
         return result.text
         checkNum()

state = getNum()

print(state)
while(1):# checks to see if there was a change in the input
        state = getNum()
        if state == oldstate:
                pass
        elif state == "1":
                 turnOn()
        else:
                 turnOff()
        oldstate = state

