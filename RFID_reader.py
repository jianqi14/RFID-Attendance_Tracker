import RPi.GPIO as GPIO

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Read Information from Card")

try:
	repeatRead = True

	while(repeatRead == True):
		print("Hold Card/Tag near the reader!")
		id, text = reader.read()

		print("Item Read, these are the information on the Card/Tag:")
		print("\n\tCard ID Number: ", id)
		print("\tCard Message: ", text)


		print("\nWould you like to read another Card/Tag?")
		readAgain = input("Enter Yes/No: ")

		if readAgain == "No" or readAgain == "no" or readAgain == 'n' or readAgain == 'N':
			repeatRead = False
			print("\n RFID Reader Ended. \n Thank You, See you Later.")

		elif readAgain == "Yes" or readAgain == "yes" or readAgain == 'Y' or readAgain == 'y':
			repeatRead = True
			print("\n")

finally:
	GPIO.cleanup()
