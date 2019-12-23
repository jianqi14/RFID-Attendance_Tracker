import RPi.GPIO as GPIO
import datetime

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
now = datetime.datetime.now()

print("RFID Card & Tag Writer\n")

try:
	userName = input('Enter New Name: ')
	print("Place Card/Tag over sensor!")

	reader.write(userName)
	print("\nMessage Overwritten Complete.")
	print(now.strftime("\n\tCurrent Date & Time: %Y-%m-%d %H:%M:%S"))
	print("\tCardHolder Name: ", userName)

	print("\nRFID Writer Ended")
	print("Thank You, See you Later\n")

finally:
	GPIO.cleanup()
