import requests

def SendData():

    url_server = "http://10.30.134.12:8011/drones" #da modificare
    json_drone_data = "json_data.json"

    req = requests.post(url_server, data = json_drone_data)

    if req.status_code == 200:
        print("Invio del JSON al Server andato a buon fine")

if __name__ == "__main__":
    SendData()