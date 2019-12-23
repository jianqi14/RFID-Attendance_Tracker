import RPi.GPIO as GPIO
import datetime

import time

# Library for the RFID
from mfrc522 import SimpleMFRC522

#setting up GPIO for buzzer
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

#setting variables for RFID
reader = SimpleMFRC522()
now = datetime.datetime.now()

print("RFID Card & Tag Writer\n")

#function of making the buzzing sound
def buzzer3Times():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.1)

	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.1)

	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.1)

try:
	userName = input('Enter New Name: ')
	print("Place Card/Tag over sensor!")

	reader.write(userName)
	buzzer3Times()
	print("\nMessage Overwritten Complete.")
	
	print(now.strftime("\n\tCurrent Date & Time: %Y-%m-%d %H:%M:%S"))
	print("\tCardHolder Name: ", userName)

	print("\nRFID Writer Ended")
	print("Thank You, See you Later\n")

finally:
	GPIO.cleanup()
