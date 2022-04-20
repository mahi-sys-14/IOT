import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(myClient, userdata, flags, rc):
	print("Connected with mqt client with result "+str(rc))

myClient = mqtt.Client()
myClient.on_connect = on_connect	#callback function
#myClient.on_message = on_message	#callback function

myClient.connect("localhost", 1883, 60)

myClient.loop_start()

while(True):
	try:
#		print("Connected")
		myClient.publish("iot/demo/lab1","Hello World")
		print("message published")
		time.sleep(1)
	except(KeyboardInterrupt): #graceful exit
		print("Graceful Exit")
		break
