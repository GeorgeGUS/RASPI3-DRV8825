# -*- coding: utf-8 -*-

# Import
import RPi.GPIO as GPIO
import pigpio
import time as t
import sys

# PINS
dirpin = 16
m0 = 11
m1 = 13
m2 = 15

# Variables
#a
#c
#d
#t
#y
z = 0
b = 0
f = 0

# configuration
def stroke():
    print("---------------------------------")

pi = pigpio.pi()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pigpio.exceptions = False
pi = pigpio.pi()

stroke()
print("https://github.com/dan-nkl/RASPI3-DRV8825")
print("For help '?' or see Github")
t.sleep(1)
stroke()
print("|       |    CONFIG     |       |")
stroke()
print('PWM-Pin  : 12')
print('Direction: 16')
GPIO.setup(dirpin, GPIO.OUT)
GPIO.output(dirpin, 0)
print('Mode0    : 11')
GPIO.setup(m0, GPIO.OUT)
GPIO.output(m0, 0)
print('Mode1    : 13')
GPIO.setup(m1, GPIO.OUT)
GPIO.output(m1, 0)
print('Mode2    : 15')
GPIO.setup(m2, GPIO.OUT)
GPIO.output(m2, 0)
stroke()
t.sleep(1)
print("Waiting for input...")
stroke()
if sys.version[0] < "3":
    input = raw_input

while(1):
    x = input('>> ').lower()

    # Start
    if x == 'start':
        try:
            pi.hardware_PWM(18, z, y)
            stroke()
            print("Program started")
            stroke()
            b = 1
            continue
        except Exception:
            stroke()
            print("Enter Freq and DC first")
            stroke()
            continue

    # Pause
    if (x == 'stop' or x == 'pause'):
        if b == 1:
            pi.hardware_PWM(18, 0, 0)
            stroke()
            print("Program paused")
            stroke()
            b = 0
            continue
        if b == 0:
            stroke()
            print("Nothing to pause")
            stroke()
            continue

    if x == '1/1':
        stroke()
        print("Full Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 0)
        GPIO.output(m2, 0)
        stroke()
        continue

    if x == '1/2':
        stroke()
        print("Half Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 0)
        GPIO.output(m2, 0)
        stroke()
        continue

    if x == '1/4':
        stroke()
        print("1/4 Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 1)
        GPIO.output(m2, 0)
        stroke()
        continue

    if x == '1/8':
        stroke()
        print("1/8 Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 1)
        GPIO.output(m2, 0)
        stroke()
        continue

    if x == '1/16':
        stroke()
        print("1/16 Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 0)
        GPIO.output(m2, 1)
        stroke()
        continue

    if x == '1/32':
        stroke()
        print("1/32 Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 0)
        GPIO.output(m2, 1)
        stroke()
        continue

    # Help
    if (x == '?' or x == 'help'):
        stroke()
        print("|       |      HELP      |      |")
        stroke()
        print("https://github.com/dan-nkl/RASPI3-DRV8825")
        print("For help see Github")
        print(" ")
        print("Commands:")
        print("'<freq> <dc>' to set Frequency and Duty cycle")
        print("'1/1'..'1/8'..'1/32' for changing step size")
        print("'start' to start the PWM")
        print("'stop' to stop the PWM")
        print("'exit' closes the program")
        stroke()
        continue

    #Direction
    if x == 'dir':
        if f == 0:
            GPIO.output(16, 1)
        if f == 1:
            GPIO.output(16, 0)
        stroke()
        print("Direction changed")
        stroke()
        continue

    # Exit
    if x == 'exit':
        stroke()
        print("Closing program")
        stroke()
        stroke()
        if b == 1:
            pi.hardware_PWM(18, 0, 0)
        t.sleep(1)
        raise SystemExit

    try:
        a, c = x.split()
        z = int(a)
        d = int(c)
        y = d*10000
    except Exception:
        stroke()
        print("Check input")
        stroke()
        continue

    if y > 1000000:
        stroke()
        print("Duty cycle can not be over 100%")
        stroke()
        continue

    stroke()
    print("Frequency : " + str(z))
    print("Duty cycle: " + str(d))
    stroke()