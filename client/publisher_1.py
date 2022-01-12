import paho.mqtt.client as mqtt
import time
import random 
import json
import os



#drone class
class Drone():

    def __init__(self,nome,id,velocita,posizione):
        self.nome = nome
        self.id = id
        self.velocita = velocita
        self.posizione = posizione





#broker 

mqttBroker = "test.mosquitto.org"
#mqttBroker = "192.168.1.116:1883"


#publisher

publisher_name="ladrone"
client = mqtt.Client(publisher_name)

client.connect(mqttBroker)

#dati randomici

def Dati():

    while True:
            #nome
            #client.publish("NOME", publisher_name) 

            #id
            id = 69420
            #client.publish("NOME/ID", id)

            #sensore velocità
            velocita = random.randrange(0,30)
            #client.publish("NOME/ID/VELOCITA", velocita)
            
            #sensore di distanza
            posizione = random.randrange(0,1000)
            #client.publish("NOME/ID/DISTANZA", distanza)
            
            #newData = Drone(publisher_name,id,velocita,distanza)

            #store(newData)

            send_msg = {
                "NOME":publisher_name,
                "ID":id,
                "VELOCITA":velocita,
                "POSIZIONE":posizione
            }

            client.publish("NOME/ID", payload=json.dumps(send_msg))

            print(f"NOME: {publisher_name}, ID: {id}, VELOCITA: {velocita}, POSIZIONE: {posizione}")

            time.sleep(1)

if __name__ == "__main__":
    Dati()