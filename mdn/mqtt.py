import paho.mqtt.client as mqtt
import json

from tracking.models import Location


def on_connect(client, userdata, flags, rc):
    print('MQTT consumer connected')
    client.subscribe('mdn/#')


def on_message(client, userdata, message):
    print(f'received message on topic {message.topic}. Payload: {message.payload}')

    data = json.loads(message.payload)

    # reply
    if 'driver_id' in data:
        print(f'reply message on topic {message.topic}')
        payload = json.dumps({'lat': lat, 'lng': lng})
        client.publish('mdn', payload)


def run_mqtt_consumer():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('rabbitmq', 1883)
    client.loop_start()
