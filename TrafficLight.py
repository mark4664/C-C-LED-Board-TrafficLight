#!/usr/bin/python3

# Script name: TrafficLight.py
# Uses the red, yellow and green LEDs to simulate a road traffic light
# 
# Mark Bradley
# 10/10/2019

# 19/11/19
# Code divided into functions and methods of exiting cleanley added.
# 1. It never exits, to stop it you have to use <ctrl> + c or click the stop button in Thonny
# 2. It does not exit cleanly, which ever LED is ON on exit is left ON.
# 20/11/19
# Develpment branch to deal with above issues.

# Import additional libraries.
from gpiozero import LED          #Using gpiozero library, LED object used for each LED
from time import sleep            #Use sleep funtion for timing, time is in seconds

def init():
    # Setup the IO pins that the LEDs are to be connected to.
    grn_led=LED(17)       # Assign pin 17 to the green led.
    yel_led=LED(18)       # Assign pin 18 to the yellow led.
    red_led=LED(19)       # Assign pin 19 to the red led.

def traffic_lights():
    # Run through a single sequence of traffic lights
    red_led.on()       # Turn LED ON, set output pin 'on' this puts +3.3v on the IO pin.
    sleep(4)           # Wait 4 seconds
    yel_led.on()       # Repeat for the other LEDs
    sleep(1)
    red_led.off()
    yel_led.off()      # Turn LED OFF, set output pin 'off' this puts 0v on the IO pin.
    grn_led.on()
    sleep(4)
    grn_led.off()
    yel_led.on()
    sleep(1.5)
    yel_led.off()
    
def clean_exit():
    # On exit turn all the LEDs off.
    grn_led.off()
    red_led.off()
    yel_led.off()
    

#------ Start of the main block of code ------

print("Traffic Light simulation programme")
init()

try:
    while True:            # Run util stopped by keyboard interrupt....Ctrl + C
        traffic_lights()
except (KeyboardInterrupt):
    clean_exit()
    
print('All Done')
        
        
        
        
