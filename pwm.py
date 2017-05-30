#!/usr/bin/env python
# encoding: utf-8

"""pwm.py: Script for controlling DRV8825 StepperMotorDrivers"""
__author__ = "Maurice Seifert"
__credits__ = "Daniel Nikulin"
__license__ = "MIT"
__version__ = "1.0.0"

# Import
import sys
import time as t
import RPi.GPIO as GPIO
import pigpio

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

# Configuration
def stroke():
    print("---------------------------------")
    
    # Start
def startprog():
    pi.hardware_PWM(18, z, y)
    stroke()
    print("Program started")
    stroke()
    

def startfail():
    stroke()
    print("Enter Freq and DC first")
    stroke()

    # Pause
def pauseprog():
    pi.hardware_PWM(18, 0, 0)
    stroke()
    print("Program paused")
    stroke()

def pausefail():
    stroke()
    print("Nothing to pause")
    stroke()

    # Exit
def exitsteps():
    stroke()
    print("Closing program")
    stroke()
    stroke()
    GPIO.cleanup()
    if b == 1:
        pi.hardware_PWM(18, 0, 0)
    t.sleep(1)
    raise SystemExit

    # Help
def helptext():
    stroke()
    print("|       |      HELP      |      |")
    stroke()
    print("https://github.com/dan-nkl/RASPI3-DRV8825")
    print("For more information see Github")
    print(" ")
    print("Command reference:")
    print("'<freq> <dc>' to set Frequency and Duty cycle")
    print("'1/1'..'1/8'..'1/32' to change step size")
    print("'start' to start the PWM")
    print("'stop' to stop the PWM")
    print("'exit' closes the program")
    print("'?' shows this information")
    stroke()

    # Direction
def changedirect():
    if f == 0:
        GPIO.output(dirpin, 1)
        f = 1
    elif f == 1:
        GPIO.output(dirpin, 0)
        f = 0
    stroke()
    print("Direction changed")
    stroke()


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
            b = 1
            t.sleep(0.1)
            startprog()
            continue
        except Exception:
            startfail()
            continue

    # Pause
    elif (x == 'stop' or x == 'pause'):
        if b == 1:
            pauseprog()
            b = 0
        elif b == 0:
            pausefail()
        continue

    # Help
    elif (x == '?' or x == 'help'):
        helptext()
        continue

    # Direction
    elif x == 'dir':
        changedirect()
        continue

    # Exit
    elif x == 'exit':
        exitsteps()

    # Steps
    elif x == '1/1':
        stroke()
        print("Full Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 0)
        GPIO.output(m2, 0)
        stroke()
        continue

    elif x == '1/2':
        stroke()
        print("Half Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 0)
        GPIO.output(m2, 0)
        stroke()
        continue

    elif x == '1/4':
        stroke()
        print("1/4 Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 1)
        GPIO.output(m2, 0)
        stroke()
        continue

    elif x == '1/8':
        stroke()
        print("1/8 Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 1)
        GPIO.output(m2, 0)
        stroke()
        continue

    elif x == '1/16':
        stroke()
        print("1/16 Step")
        GPIO.output(m0, 0)
        GPIO.output(m1, 0)
        GPIO.output(m2, 1)
        stroke()
        continue

    elif x == '1/32':
        stroke()
        print("1/32 Step")
        GPIO.output(m0, 1)
        GPIO.output(m1, 0)
        GPIO.output(m2, 1)
        stroke()
        continue

    try:
        a, c = x.split()
        z = int(a)
        d = int(c)
        y = d*10000
    except Exception:
        stroke()
        print("Check input")
        print("For help '?'")
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
