import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
while True: # Run forever
 GPIO.output(26, GPIO.HIGH) # Turn on
 GPIO.output(36, GPIO.LOW)
 sleep(1) # Sleep for 1 second
 GPIO.output(26, GPIO.LOW) # Turn off
 GPIO.output(36, GPIO.HIGH)
 sleep(1) # Sleep for 1 second
