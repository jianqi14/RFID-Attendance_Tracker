import RPi.GPIO as GPIO

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("RFID Card & Tag Writer\n")

try:
	text = input('Enter Message: ')
	print("Place Card/Tag over sensor!")

	reader.write(text)
	print("OverWritten Message Complete.\n")

	print("\t", text)

finally:
	GPIO.cleanup()
