#import requirements
import urequests
import machine

#connect to wifi

wemo_ip = '10.3.0.9'
plug_name = 'piu-plug'

led = machine.Pin(0, machine.Pin.OUT)
led.high()


do_connect()

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')


url = 'http://%s:5000/api/device/%s' % (wemo_ip, plug_name)
headers = {'Content-Type' : 'text/json; charset=utf-8'}
data = '{state: toggle}'
resp = urequests.post(url, data=data, headers=headers)
print(resp.json())

#machine.deepsleep()
