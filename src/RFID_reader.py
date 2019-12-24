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

print("RFID Card & Tag Reader\n")

#function of making the buzzing sound
def buzzerSound():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.35)
	
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.15)

def infoDisplay():
		print("Item Read, these are the information on the Card/Tag:")
		print(now.strftime("\n\tDate & Time: %Y-%m-%d %H:%M:%S"))
		print("\tCard ID Number:", id)
		print("\tCardHolder Name:", userName)

try:
	repeatRead = True

	while(repeatRead == True):
		print("Place Card/Tag over sensor!")
		id, userName = reader.read()

		buzzerSound()
		infoDisplay()

		#Ask User if they want to read another Card
		print("\nWould you like to read another Card/Tag?")
		readAgain = input("Enter Yes/No: ")

		if readAgain == "No" or readAgain == "no" or readAgain == 'n' or readAgain == 'N':
			repeatRead = False
			print("\n RFID Reader Ended. \n Thank You, See you Later.\n")

		elif readAgain == "Yes" or readAgain == "yes" or readAgain == 'Y' or readAgain == 'y':
			repeatRead = True
			print("\n")
		#End of asking user to read again.

finally:
	GPIO.cleanup()
