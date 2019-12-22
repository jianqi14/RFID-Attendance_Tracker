import RPi.GPIO as GPIO

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Write new information onto a Card")

try:
	text = input('Enter Message: ')
	print("Place Card over sensor")

	reader.write(text)
	print("OverWritten Complete.")

	print(text)

finally:
	GPIO.cleanup()
