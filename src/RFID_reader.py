import RPi.GPIO as GPIO
import datetime

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
now = datetime.datetime.now()

print("RFID Card & Tag Reader\n")

try:
	repeatRead = True

	while(repeatRead == True):
		print("Place Card/Tag over sensor!")
		id, userName = reader.read()

		print("Item Read, these are the information on the Card/Tag:")

		print(now.strftime("\n\tDate & Time: %Y-%m-%d %H:%M:%S"))
		print("\tCard ID Number:", id)
		print("\tCardHolder Name:", userName)

		print("\nWould you like to read another Card/Tag?")
		readAgain = input("Enter Yes/No: ")

		if readAgain == "No" or readAgain == "no" or readAgain == 'n' or readAgain == 'N':
			repeatRead = False
			print("\n RFID Reader Ended. \n Thank You, See you Later.\n")

		elif readAgain == "Yes" or readAgain == "yes" or readAgain == 'Y' or readAgain == 'y':
			repeatRead = True
			print("\n")

finally:
	GPIO.cleanup()
