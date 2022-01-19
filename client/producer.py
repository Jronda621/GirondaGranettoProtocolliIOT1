
import time
import random 
import json
import os
import pika



#drone class
class Drone():

    def __init__(self,nome,id,velocita,posizione):
        self.nome = nome
        self.id = id
        self.velocita = velocita
        self.posizione = posizione


publisher_name="ladrone"
CONNECTION_STRING = ""




#dati randomici

def Dati():

    while True:
            id = 69420

            velocita = random.randrange(0,30)

            posizione = random.randrange(0,1000)

            send_msg = {
                "NOME":publisher_name,
                "ID":id,
                "VELOCITA":velocita,
                "POSIZIONE":posizione
            }

            #client.publish("PROGETTO_DRONE/NOME/ID", payload=json.dumps(send_msg))
            url = os.environ.get('CLOUDAMQP_URL', CONNECTION_STRING)
            params = pika.URLParameters(url)
            connection = pika.BlockingConnection(params)
            channel = connection.channel() # start a channel
            channel.queue_declare(queue='queue1') # Declare a queue
            channel.basic_publish(exchange='',
                                routing_key='queue1',
                                body=str(json.dumps(send_msg)))

            print(" [x] Sent data")
            connection.close()
            print(f"NOME: {publisher_name}, ID: {id}, VELOCITA: {velocita}, POSIZIONE: {posizione}")

            time.sleep(0.5)

if __name__ == "__main__":
    if CONNECTION_STRING == "": 
        print("Inserire i dati di connessione su CONNECTION_STRING")
    else:
        Dati()