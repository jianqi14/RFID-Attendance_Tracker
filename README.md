
# MFRC522 RFID Read & Write

## Pin layout

These are the pins used when connecting the Raspberry Pi and the MFRC522 RFID together.

|Raspberry Pi     | RFID     |
|-----------------|----------|
| Pin 1           |  3.3v    |
| Pin 22          |  RST     |
| Pin 6           |  GND     |
| Pin 21          |  MISO    |
| Pin 19          |  MOSI    |
| Pin 23          |  SCK     |
| Pin 24          |  SDA     |

|Buzzer	| input	| outPut|
|-------|-------|-------|
|	    |Pin 12 | GND	|

---

## Items and Technologies used for built

The Items I used to build this project was a Raspberry Pi 3 Model B, some Jumper wires, a MFRC522 RFID Read & Write, breadboard, and some RFID Cards & Tags.

The technologies I will use are Python, HTML, CSS, and SQL. More technologies might be added but these are for certain.

There is also a Buzzer noise for confirmation to let the user know when the RFID had processed a task. The Pin that the Buzzer will occupied on Raspberry pi board is Pin 12.

What if we use google spreadsheet API to store user name, time stamp, etc.

I will also plan to use Solidworks CAD design to build an outer frame to house the Raspberry Pi, RFID reader and all other componets into a 3D printed case.

---

## How to run RFID Python Programs

I have 2 programs availble for this RFID Project. One program is for reading data from RFID cards and another is meant for writing new data into the RFID cards. The program for reading data using the RFID is called RFID_reader.py and for writing data is called RFID_writer.py. 

Both the read and write programs uses Python. You will need to open Terminal to run these code individually. Make sure you are at the correct directory before running the program. Once you at the correctory directory where both ```RFID_reader.py``` and ```RFID_writer.py``` are located at, run the following command below to execute them.

Read a RFID Card, Enter the following Command:
```
python3 RFID_reader.py
```

Write a RFID Card, Enter the following Command:
```
python3 RFID_reader.py
```

---