import paho.mqtt.client as mqtt
import time
import json
import os

#ogni volta che riceviamo un messaggio
def on_message(client, userdata, message):
    print("Messaggio ricevuto: ", json.loads(message.payload.decode("utf-8")))


#broker 

mqttBroker = "mqtt.eclipseprojects.io"
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




time.sleep(10)

client.loop_stop()



