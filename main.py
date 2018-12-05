import dht
import json
import machine
import time
from umqtt.simple import MQTTClient


with open('config.json', 'r') as c:
    config = json.load(c)

# Emulate a pull-up resistor
pin = machine.Pin(config['sensor']['pin'], machine.Pin.IN, machine.Pin.PULL_UP)
# Set up our sensor pins
sensor = dht.DHT22(machine.Pin(config['sensor']['pin']))
# Set up the RTC for DEEPSLEEP
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

while True:
    # Take our readings
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()

    print('The temperature is', temperature, '°C')
    print('The humidity is', humidity, '%')

    # Establish our MQTT connection
    client = MQTTClient(config['mqtt']['user'],
                        config['mqtt']['broker'],
                        user=config['mqtt']['user'],
                        password=config['mqtt']['password'],
                        port=1883)
    client.connect()

    client.publish(config['mqtt']['topic'] + '/temperature', bytes(str(temperature), 'utf-8'))
    client.publish(config['mqtt']['topic'] + '/humidity', bytes(str(humidity), 'utf-8'))
    client.disconnect()
    print('Published to broker', config['mqtt']['broker'], 'on topic', config['mqtt']['topic'], 'Successfully.')

    time.sleep(300)
