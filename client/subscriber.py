import paho.mqtt.client as mqtt
import time
import json
import os
import requests

msg_received = {}

#ogni volta che riceviamo un messaggio
def on_message(client, userdata, message):
    msg_received = json.loads(message.payload.decode("utf-8"))
    print("Messaggio ricevuto: ", json.loads(message.payload.decode("utf-8")))
    #print(msg_received)

#broker 

mqttBroker = "test.mosquitto.org"
#mqttBroker = "192.168.1.116:1883"

#publisher

subscriber_name="subscriber"
client = mqtt.Client(subscriber_name)

client.connect(mqttBroker)

#topic loop --> rimane in ascolto ogni 

client.loop_start()

#scelta del topic a cui iscriversi
client.subscribe("NOME/ID")

#ricezione messaggio
client.on_message = on_message

print("Effettuo richiesta API")
#response = requests.post("localhost:9000/drones/"+msg_received.ID)


time.sleep(1)

client.loop_stop()



