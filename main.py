import dht
import json
import machine


with open('config.json', 'r') as c:
    config = json.load(c)

# Set up our sensor pins
sensor = dht.DHT22(machine.Pin(config['sensor']['pin']))

# Take our readings
sensor.measure()

print('The temperature is', sensor.temperature(), '°C')
print('The humidity is', sensor.humidity(), '°C')
