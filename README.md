
# MFRC522 RFID Attendance Tracker:

## About:

I am a recent University Graduate on May 2020 who studied Computer Science and I'm a current Volunteer Teaching Assistant at a Non-profit called Dev-Mission. For the Non-profit, I've built a project where I could make an impact on providing students a more intuitive and seamless method in taking attendance whenever students arrives and leave class. Through my courses that I've taken at my University, one of my favorite classes were Human-Computer Interaction and I believe that the way we interact with technology is important!

Throughout this page, I would be describing the technologies (Software & Hardware) I've used and a UI Webpage Design where students will be interacting with when they arrives and leave the non-profit office.

I am constantly improving this project everyday and I hope that someday I could finalize this project into reality!!

---

## UI Webpage Design: RFID Attendance Tracker:

These are a few Webpage Designs I've made for students once they had arrived to get check in and departure the office.

This is the UI Home Webpage that all students would see once they arrive and leave class. The Webpage would provide details such as the current live Date & Time on the upper left corner of the page and a Logout button for the staffs to exit the Webpage software. 
<img width="566" alt="Screen Shot 2021-02-15 at 10 57 35 PM" src="https://user-images.githubusercontent.com/40045109/108029559-80417e80-6fe2-11eb-844c-024323b01d57.png">

Once the students successfully gotten Checked-In, this would be the UI Webpage students would see. The UI Webpage would display the Student's photo, name, welcome note and the time they had Checked-In. 
<img width="565" alt="Screen Shot 2021-02-15 at 11 01 34 PM" src="https://user-images.githubusercontent.com/40045109/108029554-7ae43400-6fe2-11eb-82de-2af20cd27998.png">

Finally, when students leaves the office, the UI Webpage would display a Thank you page of the Student's photo, name & the time they Checked-Out. 
<img width="566" alt="Screen Shot 2021-02-15 at 11 01 44 PM" src="https://user-images.githubusercontent.com/40045109/108029533-73bd2600-6fe2-11eb-8767-e934084e00a1.png">

---

## Pin layout:

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

## Items and Technologies used for built:

The Items I used to build this project was a Raspberry Pi 3 Model B, some Jumper wires, a MFRC522 RFID Read & Write, breadboard, and some RFID Cards & Tags.

The technologies I will use are Python, HTML, CSS, and SQL. More technologies might be added but these are for certain.

There is also a Buzzer noise for confirmation to let the user know when the RFID had processed a task. The Pin that the Buzzer will occupied on Raspberry pi board is Pin 12.

What if we use google spreadsheet API to store user name, time stamp, etc.

I will also plan to use Solidworks CAD design to build an outer frame to house the Raspberry Pi, RFID reader and all other componets into a 3D printed case.

---

## How to run RFID Python Programs:

I have 2 programs availble for this RFID Project. One program is for reading data from RFID cards and another is meant for writing new data into the RFID cards. The program for reading data using the RFID is called RFID_reader.py and for writing data is called RFID_writer.py. 

Both the read and write programs uses Python. You will need to open Terminal to run these code individually. Make sure you are at the correct directory before running the program. Once you at the correctory directory where both ```RFID_reader.py``` and ```RFID_writer.py``` are located at, run the following command below to execute them.

Read a RFID Card, Enter the following Command:
```
python3 RFID_reader.py
```

Write a RFID Card, Enter the following Command:
```
python3 RFID_writer.py
```

---
