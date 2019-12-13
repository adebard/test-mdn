import paho.mqtt.client as mqtt
from random import uniform
import time
import json
import threading


nclients = 20
clients = []


def new_point():
    # New lat/lng position.
   return uniform(-180,180), uniform(-90, 90)


def create_clients():
    for i in range(nclients):
        print(f'client created {i}')
        client_name = str(i)
        client = mqtt.Client(client_name)
        client.will_set('mdn', 'LOST_CONNECTION', 0, False)
        client.connect('0.tcp.ngrok.io', 11756)
        clients.append(client)


def simulate_gps(client, client_number):
    while True:
        lat, lng = new_point()
        print(f'driver {client_number} sending new location {lat}, {lng}')
        payload = json.dumps({'driver_id': client_number, 'lat': lat, 'lng': lng})
        client.publish('mdn', payload)
        time.sleep(5)


if __name__ == '__main__':
    create_clients()
    for i in range(nclients):
        client = clients[i]
        # For each client throw a thread that simulates the GPS.
        thread = threading.Thread(target=simulate_gps, args=(client, i))
        thread.start()
