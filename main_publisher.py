import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

while True:
    client.publish("vs25/sebastian/temp", "22.4")
    time.sleep(15)


    