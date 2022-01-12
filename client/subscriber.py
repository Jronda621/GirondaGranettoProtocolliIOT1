import paho.mqtt.client as mqtt
import time
import json
import os
import requests

msg_received = {}
API_URL = "http://localhost:9000/drones"

#ogni volta che riceviamo un messaggio
def on_message(client, userdata, message):
    msg_received = json.loads(message.payload.decode("utf-8"))
    print(msg_received)

    r = requests.post(url = API_URL, data ="", json=msg_received)
    pastebin_url = r.text 
    print(pastebin_url)   
    #print("Messaggio ricevuto: ", json.loads(message.payload.decode("utf-8")))
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

print("entro nel loop")


#scelta del topic a cui iscriversi

client.subscribe("PROGETTO_DRONE/NOME/ID")

#ricezione messaggio
client.on_message = on_message
#print("Client on message: " + on_message)


time.sleep(30)  # DA VERIFICARE PERCHè CICLA UNA SOLA VOLTA

client.loop_stop()




