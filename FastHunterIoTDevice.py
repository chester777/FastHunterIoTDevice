import os
import sys
import random
import time

def makeBLEPacket() :

	###### this section is about Bluetooth Device Module Setting
	BLE_DEVICE = "hci0"

	############################################################

	###### this section is about Bluetooth Protocol Stack
	OGF = "0x08"
	OCF = "0x0008" # means # means that it is using iBeacon Protocol Stack

	BEACON_PREFIX = "1E 02 01 1A 1A FF 4C 00 02 15" # means that it is using iBeacon Protocol Stack

	UUID = {}
	UUID[1] = "4a 4e ce 60 7e b0 11 e4 b4 a9 08 00 20 0c 9a 66" # GasLock UUID
	UUID[2] = "a1 df 3a 93 3a a8 4d af b9 e0 2a 4a aa 1d 44 3d" # DoorLock UUID
	UUID[3] = "9b f6 42 0e ad 0b 4d 89 90 2f 1b 58 15 07 5f ac" # AirConditionerUUID
	UUID[4] = "b4 c6 75 da 5c a0 43 2e a1 c7 0b 3a ee ae 7f 9f" # GasBoiler UUID
	UUID[5] = "cb fd 2b 61 a8 41 43 5f ae fa f9 fe 2c 05 4f 6c" # Lightware Oven UUID
	UUID[6] = "71 1f e8 95 e1 35 45 6e 9d 22 08 96 d8 a5 a4 4e" # Smart Switch UUID
	UUID[7] = "07 fd 21 93 98 92 4e cc ae bb bb 15 51 bd e0 b2" # Power Meter UUID

	DEVICE_NO = random.randrange(1,8)
	MajorData = "" # means device status
	MinorData = "" # means device value

	if DEVICE_NO == 1 :
		uuid = UUID[1]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 8 :
			MajorData = "00 00"
			MinorData = "00 00"
		elif 8 <= statusExpect < 10 :
			MajorData = "00 01"
			MinorData = "00 00"

	elif DEVICE_NO == 2 :
		uuid = UUID[2]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 8 :
			MajorData = "00 00"
			MinorData = "00 00"
		elif 8 <= statusExpect < 10 :
			MajorData = "00 01"
			MinorData = "00 00"

	elif DEVICE_NO == 3 :
		uuid = UUID[3]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 7 : # normal status
			temperatrue = random.randrange(18, 26)
			MajorData = "00 01" 
			MinorData = "00 " + str(temperatrue)

		elif 7 <= statusExpect < 8 : # abnormal status (status :0, value exist)
			temperatrue = random.randrange(18, 26)
			MajorData = "00 00"
			MinorData = "00 " +  str(temperatrue)

		elif 8 <= statusExpect < 9 : # abnormal status (value is not in normal range)
			tempRandom = random.randrange(0,2)

			if tempRandom == 0 :
				temperatrue = random.randrange(1, 17)
			elif tempRandom == 1:
				temperatrue = random.randrange(25, 100)

			MajorData = "00 01"
			MinorData = "00 " +  str(temperatrue)

		elif 9 <= statusExpect < 10 : # status change
			MajorData = "00 01"
			MajorData = "99 99"

	elif DEVICE_NO == 4 :
		uuid = UUID[4]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 7 : # normal status
			temperatrue = random.randrange(70, 90)
			MajorData = "00 01" 
			MinorData = "00 " + str(temperatrue)

		elif 7 <= statusExpect < 8 : # abnormal status (status :0, value exist)
			temperatrue = random.randrange(70, 90)
			MajorData = "00 00"
			MinorData = "00 " +  str(temperatrue)

		elif 8 <= statusExpect < 9 : # abnormal status (value is not in normal range)
			temperatrue = random.randrange(90, 100)

			MajorData = "00 01"
			MinorData = "00 " +  str(temperatrue)

		elif 9 <= statusExpect < 10 : # status change
			MajorData = "00 01"
			MajorData = "99 99"

	elif DEVICE_NO == 5 :
		uuid = UUID[5]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 7 : # normal status
			temperatrue = random.randrange(150, 200)
			MajorData = "00 01" 
			MinorData = "00 " + str(temperatrue)

		elif 7 <= statusExpect < 8 : # abnormal status (status :0, value exist)
			temperatrue = random.randrange(150, 200)
			MajorData = "00 00"
			MinorData = "00 " +  str(temperatrue)

		elif 8 <= statusExpect < 9 : # abnormal status (value is not in normal range)
			temperatrue = random.randrange(200, 1000)

			MajorData = "00 01"
			MinorData = "00 " +  str(temperatrue)

		elif 9 <= statusExpect < 10 : # status change
			MajorData = "00 01"
			MajorData = "99 99"

	elif DEVICE_NO == 6 :
		uuid = UUID[1]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 8 :
			MajorData = "00 00"
			MinorData = "00 00"
		elif 8 <= statusExpect < 10 :
			MajorData = "00 01"
			MinorData = "00 00"

	elif DEVICE_NO == 7 :
		uuid = UUID[1]
		statusExpect = random.randrange(0, 10)

		if 0 <= statusExpect < 8 :
			power = random.randrange(300, 501)
			MajorData = "00 00"
			MinorData = "00 " + str(power)
		elif 8 <= statusExpect < 10 :
			power = random.randrange(1000, 2000)
			MajorData = "00 01"
			MinorData = "00 " + str(power)

	Power = "C5 00"

	############################################################

	os.system("sudo hciconfig " + BLE_DEVICE + " up")
	os.system("sudo hciconfig " + BLE_DEVICE + " noleadv")
	os.system("sudo hciconfig " + BLE_DEVICE + " noscan")
	os.system("sudo hciconfig " + BLE_DEVICE + " pcsan")
	os.system("sudo hciconfig " + BLE_DEVICE + " leadv")

	#advertising
	print "Device No:" + str(DEVICE_NO)
	print "Major Data:" + str(MajorData)
	print "Minor Data:" + str(MinorData)
	os.system("sudo hcitool -i " + BLE_DEVICE + " cmd " + OGF + " " + OCF + " " + BEACON_PREFIX + " " + uuid + " " + MajorData + " " + MinorData + " " + Power)

if __name__ == '__main__' :
	try :
		while True :
			makeBLEPacket()
			time.sleep(0.1)
	except KeyboardInterrupt :
		pass
