#!/usr/bin/python3

# Script name: TrafficLight.py
# Uses the red, yellow and green LEDs to simulate a road traffic light
# 
# Mark Bradley
# 10/10/2019

# 19/11/19
# Code divided into functions and a method of exiting cleanley added.
# To exit the code use <ctrl> + c or click the stop button in Thonny


# Import additional libraries.
from gpiozero import LED          #Using gpiozero library, LED object used for each LED
from gpiozero import Button
from time import sleep            #Use sleep funtion for timing, time is in seconds

# Setup the IO pins that the LEDs are to be connected to.
grn_led=LED(17)       # Assign pin 17 to the green led.
yel_led=LED(18)       # Assign pin 18 to the yellow led.
red_led=LED(19)       # Assign pin 19 to the red led.
btn1=Button(21)       # Assign pin 21 to button 1 (btn1)

def traffic_lights():
    # Run through a single sequence of traffic lights
    red_led.on()       # Turn LED ON, set output pin 'on' this puts +3.3v on the IO pin.
    sleep(2)           # Wait 4 seconds
    yel_led.on()       # Repeat for the other LEDs
    sleep(1)
    red_led.off()
    yel_led.off()      # Turn LED OFF, set output pin 'off' this puts 0v on the IO pin.
    grn_led.on()
    sleep(2)
    grn_led.off()
    yel_led.on()
    sleep(1)
    yel_led.off()
    
def clean_exit():
    # On exit turn all the LEDs off.
    grn_led.off()
    red_led.off()
    yel_led.off()
   

#------ Start of the main block of code ------

print("Traffic Light simulation programme")
#btn1.when_pressed = btn1_pressed


try:
    while not btn1.is_pressed:    # Run utill the button is pushed
        traffic_lights()
        
except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    clean_exit()
    
print('All Done')
        
        
        
        
