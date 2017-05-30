#!/usr/bin/env python
# encoding: utf-8

"""pwm.py: Script for controlling DRV8825 StepperMotorDrivers"""
__author__ = "Maurice Seifert"
__credits__ = "Daniel Nikulin"
__license__ = "MIT"
__version__ = "1.0.1"

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
#d
#t
#y
b = 0
c = 50
e = 0
f = 0
z = 0

# Configuration
def stroke():
    """Shortened version of the output, makes the code clearer"""
    print("---------------------------------")
  
def startprog():
    """Starts the PWM output"""
    pi.hardware_PWM(18, z, y)
    stroke()
    print("Program started")
    stroke()

def startfail():
    """Error message. If start failed"""
    stroke()
    print("Enter Freq and DC first")
    stroke()

def pauseprog():
    """Stops the PWM output"""
    pi.hardware_PWM(18, 0, 0)
    stroke()
    print("Program paused")
    stroke()

def pausefail():
    """Error message. If nothing to pause"""
    stroke()
    print("Nothing to pause")
    stroke()

    # Exit
def exitsteps():
    """The steps that terminate the program"""
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
    """Displays help"""
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
    """Changes the direction of the motors"""
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
        try:
            a, c = x.split()
        except Exception:
            a = x
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
    if e == 1:
        print("Write 'start' to adopt to new values")
        e = 1
    stroke()
