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

import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://henytxme:CUG5r-L3oA9DnqE_THJZHVNeoOAsgk27@roedeer.rmq.cloudamqp.com/henytxme')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()

#scelta del topic a cui iscriversi

client.subscribe("PROGETTO_DRONE/NOME/ID")

#ricezione messaggio
client.on_message = on_message
#print("Client on message: " + on_message)


time.sleep(30)  # DA VERIFICARE PERCHè CICLA UNA SOLA VOLTA

client.loop_stop()




