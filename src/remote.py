import os
import time

from gpiozero import Button

button0 = Button(21)
button1 = Button(25)
button2 = Button(18)
button3 = Button(2)

button4 = Button(20)
button5 = Button(24)
button6 = Button(15)
button7 = Button(3)

button8 = Button(16)
button9 = Button(23)
buttonA = Button(14)
buttonB = Button(4)

os.system("cd /boot/firmware")

modes = ['N','U','L','B']

sm1 = 0
sm2 = 0

so1 = -1
so2 = -1

str_avmode = "./ortin avmode "



def buildstr():
	return str(str_avmode + str(modes[sm1]) + " " + str(modes[ sm2]))


while True:
	if button0.is_pressed:
		os.system("./ortin fullreset")

	if button1.is_pressed:
		os.system("./ortin reset")
	
	if button2.is_pressed:
		so1 = so1 * -1
		
		if so1 == 1:
			os.system("./ortin sloton 1")
		else:
			os.system("./ortin slotoff 1")
	
	if button3.is_pressed:
		so2 = so2 * -1

		if so2 == 1:
			os.system("./ortin sloton 2")
		else:
			os.system("./ortin slotoff 2")

	if button4.is_pressed:
		os.system("./ortin load /boot/firmware/rom.nds")

	if button5.is_pressed:
		os.system( buildstr())

	if button6.is_pressed:
		sm1 += 1
		sm1 %= 4
		os.system( buildstr())

	if button7.is_pressed:
		sm2 += 1
		sm2 %= 4
		os.system( buildstr())

	if button8.is_pressed:
		os.system("")

	if button9.is_pressed:
		os.system("")

	if buttonA.is_pressed:
		os.system("")

	if buttonB.is_pressed:
		os.system("")
