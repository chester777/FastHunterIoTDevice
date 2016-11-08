import os
import sys

BLE_DEVICE = "hci0"

OGF = "0x08"
OCF = "0x0008"
BEACON_PREFIX = "1E 02 01 1A 1A FF 4C 00 02 15"
UUID = "4a 4e ce 60 7e b0 11 e4 b4 a9 08 00 20 0c 9a 66"

MajorData = "00 01" # means device info
MinorData = "00 01" # means device status or data
Power = "C5 00"

os.system("sudo hciconfig " + BLE_DEVICE + " up")
os.system("sudo hciconfig " + BLE_DEVICE + " noleadv")
os.system("sudo hciconfig " + BLE_DEVICE + " noscan")
os.system("sudo hciconfig " + BLE_DEVICE + " pcsan")
os.system("sudo hciconfig " + BLE_DEVICE + " leadv")

#advertising
os.system("sudo hcitool -i " + BLE_DEVICE + " cmd " + OGF + " " + OCF + " " + BEACON_PREFIX + " " + UUID + " " + MajorData + " " + MinoData + " " + Power)
