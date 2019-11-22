#!/usr/bin/python3

# Script name: ThreadedTrafficLight.py
# Uses 2 sets the red, yellow and green LEDs to simulate traffic lights at a cross roads
# 
# Mark Bradley
# 21/11/19

# Traffic signal class used twice to create a pair of lights to control a junction.
# Stop and Go methods to set the lights as required.
# Push button on IO 21 running in a seperate thread controls termination of the code.


# Import additional libraries.
from gpiozero import LED     #Using gpiozero library, LED object used for each LED
from gpiozero import Button
from time import sleep       #Use sleep funtion for timing, time is in seconds
from threading import Thread

global but1_state  # Global value used to pass button state between the 2 threads
btn1_state=False

class button_checker:   # Push button checker running in it's own thread
    def __init__(self):
        self.btn1=Button(21)       # Assign pin 21 to button 1 (btn1)
        self._running=True
        
    def terminate(self):
        self._running=False
        
    def run(self):
        global btn1_state
        while self._running:
            if self.btn1.is_pressed == True:
                btn1_state=True
            
            print('button check ',btn1_state,'@',self.btn1.is_pressed)    
            sleep(0.5)

class traffic_signal:
    def __init__(self,grn,yel,red): # Parameters grn yel & red contain IO pins for LED
        self.grn_led=LED(grn)       # Assign pin grn to the green led (grn_led) etc.
        self.yel_led=LED(yel)       
        self.red_led=LED(red)
        self.red_led.on()           #Set the traffic signal to Red
        
    def terminate(self):
        self.grn_led.off()
        self.red_led.off()
        self.yel_led.off()
        
    def go(self):      # Change traffic signal from Red to Green
        self.yel_led.on()       
        sleep(1.5)
        self.red_led.off()
        self.yel_led.off()
        self.grn_led.on()
                    
    def stop(self):    # Change traffic signal from Green to Red
        self.grn_led.off()
        self.yel_led.on()
        sleep(2)
        self.yel_led.off()
        self.red_led.on()
    
b1=button_checker()
b1thread=Thread(target=b1.run)
b1thread.start()

tl_ns=traffic_signal(17,18,19)   # Configure traffic lights for cross roads
tl_ew=traffic_signal(20,22,23)   # North-South (ns) East-West (ew) junction


#------ Start of the main block of code ------

print("Traffic Light simulation programme - Threaded Version")


try:
    while not btn1_state:    # Run utill the button is pushed
       tl_ns.go()
       sleep(2)
       tl_ns.stop()
       sleep(2)
       tl_ew.go()
       sleep(2)
       tl_ew.stop()
       sleep(2)
        
except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    pass
  
tl_ns.terminate()  # Turn all the LEDs off
tl_ew.terminate()
b1.terminate()     # Stop the button checking thread
print('All done!')

