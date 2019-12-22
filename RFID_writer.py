import RPi.GPIO as GPIO
import datetime

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
now = datetime.datetime.now()

print("RFID Card & Tag Writer\n")

try:
	text = input('Enter Message: ')
	print("Place Card/Tag over sensor!")

	reader.write(text)
	print(now.strftime("\n\tCurrent Date & Time: ", "%Y-%m-%d %H:%M:%S"))
	print("OverWritten Message Complete.\n")

	print("\t", text)

finally:
	GPIO.cleanup()
