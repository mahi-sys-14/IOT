from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.common.auth.connection_string import DEVICE_ID
import random
import json
import time
import datetime

TEMPERATURE = 0
HUMIDITY = 0

CONNECTION_STRING = "HostName=042222-iothub-trainingday5-session-2.azure-devices.net;DeviceId=shubham011;SharedAccessKey=B6OkMOjk/8GZATBH4gXM+eRF1Ss6KdKXhrezE6M2tkU="
global DEVICEID
RECEIVED_MESSAGE = 0

#def iothub_client_init():
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
#return client


print("Azure client device initiated")
while(True):
	try:
		temperature = TEMPERATURE + (random.random() * 15)
		humidity = HUMIDITY + (random.random() * 20)

		message = {}
		currentTime = str(datetime.datetime.now())
		message["deviceid"] = "shubham011"
		message["timestamp"] = currentTime
		message["temperature"] = temperature
		message["humidity"] = humidity
		sensorval = json.dumps(message)
		client.send_message(sensorval)
		print("message send to client: " + sensorval)
		time.sleep(5)
	except KeyboardInterrupt:
		#client.disconnect()
		print("graceful Exit")
		break;
