from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.common.auth.connection_string import DEVICE_ID
import time
import datetime
import subprocess as p
import threading

CONNECTION_STRING ="HostName=042222-iothub-trainingday5-session-2.azure-devices.net;DeviceId=asdevice011;SharedAccessKey=VhGuT/teao/uc60pcwINkfbj2MNIJrjwberIs/kJzqA="

global DEVICEID
RECEIVED_MESSAGES=0

client= IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
print("azure device client initiated")
print("Waiting for event from client............")

def music1():
	m1=p.Popen(['ffplay','falak-tu-garaj-tu-kgf-chapter-2-128-kbps-sound.mp3'])
	m1.communicate()

def music2():
	m2=p.Popen(['ffplay','kudiyan-lahore-diyan-harrdy-sandhu-128-kbps-sound.mp3'])
	m2.communicate()

def message_handler(message):
	global RECEIVED_MESSAGES
	RECEIVED_MESSAGES += 1
	print("direct message "+str(message))
	str_message =  str(message)
	print("event received: "+str_message)

	if str_message[11] == "0":
		print("No Action")
	elif str_message[11] == "1":
		p.Popen(['vi' ,'file.txt'])
		print("Open file")
	elif str_message[11] == "2":
		t1 = threading.Thread(target=music1)
		t2 = threading.Thread(target=music2)

		t1.start()
		t2.start()

		time.sleep(3)
		print("open music file")
	else:
		print("Send correct event from cloud to device")

	print(" ")
	# print("Message received:" +str(message))


while(True):
	try:
		client.on_message_received=message_handler
		currentTime= str(datetime.datetime.now())

		time.sleep(5)
	except KeyboardInterrupt:
		print("graceful exit")
		break
