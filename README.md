# Skiddaw U3A C&C Group-LED-Board-TrafficLight
Threaded Traffic Lights
Each traffic signal is built from a class and controlled by calling it's methods
A push button is checked in a seperate thread and when operated it terminates the code.
Putting the button in it's own thread allows operation to be detected in 0.5 sec rather than having to wait
for the main loop to get around to checking it.

