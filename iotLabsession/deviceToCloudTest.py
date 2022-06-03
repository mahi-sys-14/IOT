from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.common.auth.connection_string import DEVICE_ID
import random
import json
import time
import datetime

TEMPERATURE = 0
HUMIDITY = 0

CONNECTION_STRING = ""
global DEVICEID

def iothub_client_init():
	client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
	return client


while(True):
	try:
		temperature = TEMPERATURE + (random.random() * 15)
		humidity = HUMIDITY + (random.random() * 20)

		message = {}
		currentTime = str(datetime.datetime.now())
		message["deviceid"] = "myDevice001"
		message["timestamp"] = currentTime
		message["temperature"] = temperature
		message["humidity"] = humidity
		sensorval = json.dumps(message)
		print("message send to client: " + sensorval)
		time.sleep(1)
	except KeyboardInterrupt:
		print("graceful Exit")
		break;
