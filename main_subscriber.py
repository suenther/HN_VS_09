import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f'{msg.topic}: {msg.payload.decode()}')

client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("vs25/sebastian/temp")
client.loop_forever()