#import requirements
#import urequests
import ubinascii
import machine
from umqtt.simple import MQTTClient
from machine import Pin
from machine import ADC
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"esp_switch"
mqtt = MQTTClient(CLIENT_ID, mqtt_server, user=mqtt_user, password=mqtt_password)


#If you have an LED linked to GPIO0 then this will turn it on. 
led = machine.Pin(0, machine.Pin.OUT)
led.high()

#connect to wifi
do_connect()

VOLT = ADC(1).read()


def trigger_button():
    data = b'{ "Power": "toggle", "Voltage": "%s" }' % VOLT
    mqtt.connect()
    mqtt.publish(TOPIC, data)
#    url = 'http://%s:5000/api/device/%s' % (wemo_ip, plug_name)
#    headers = {'Content-Type' : 'text/json; charset=utf-8'}
#    data = '{state: toggle}'
#    resp = urequests.post(url, data=data, headers=headers)
#    print(resp.json())
#	machine.deepsleep()


#if machine.reset_cause() == machine.DEEPSLEEP_RESET:
print('woke from a deep sleep')
print('Running command!')
print(CLIENT_ID)
print(mqtt_server)
print(mqtt_user)
print(mqtt_password)
trigger_button()
#else:
#    print('power on or hard reset')
    #comment this out to drop to repl for debuging.
#    machine.deepsleep()

