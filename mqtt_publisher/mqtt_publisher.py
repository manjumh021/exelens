import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()
client.connect("mqtt-broker-container", 1883, 60)  # Use the container name of the MQTT broker

while True:
    sensor_id = "unique_sensor_id"
    
    # Simulate temperature and humidity values
    temperature_value = random.uniform(0, 100)
    humidity_value = random.uniform(0, 100)
    
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    
    # Payload for temperature
    temperature_payload = {
        "sensor_id": sensor_id,
        "value": temperature_value,
        "timestamp": timestamp
    }
    
    # Payload for humidity
    humidity_payload = {
        "sensor_id": sensor_id,
        "value": humidity_value,
        "timestamp": timestamp
    }
    
    # Publish to temperature topic
    client.publish("sensors/temperature", json.dumps(temperature_payload))
    
    # Publish to humidity topic
    client.publish("sensors/humidity", json.dumps(humidity_payload))
    
    time.sleep(5)
