import network
import json
import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('Waking from deep sleep')
else:
    print('Power on or waking from a hard reset')

with open('config.json', 'r') as c:
    config = json.load(c)

# Station network device (wifi client)
sta_if = network.WLAN(network.STA_IF)
# AP network device (wifi access point)
ap_if = network.WLAN(network.AP_IF)

# Disable the AP
ap_if.active(False)

# Connect to our configured WiFi network
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(config['wifi']['ssid'], config['wifi']['password'])
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
