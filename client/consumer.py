from email import message
import paho.mqtt.client as mqtt
import time
import json
import requests
import pika, os

msg_received = {}
API_URL = "http://localhost:9000/drones"
CONNECTION_STRING = ""
if CONNECTION_STRING == "": 
  print("Inserire i dati di connessione su CONNECTION_STRING")
else:

  # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
  url = os.environ.get('CLOUDAMQP_URL', CONNECTION_STRING)
  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel() # start a channel
  channel.queue_declare(queue='hello') # Declare a queue
  def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))
    msg = json.loads(body)
    r = requests.post(url = API_URL, data ="", json=msg)
    print("Post on Mongo")

  channel.basic_consume('queue1',
                        callback,
                        auto_ack=True)

  print(' [*] Waiting for messages:')
  channel.start_consuming()
  connection.close()







