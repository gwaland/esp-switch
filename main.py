#import requirements
import urequests
import machine

#connect to wifi

#If you have an LED linked to GPIO0 then this will turn it on. 
led = machine.Pin(0, machine.Pin.OUT)
led.high()


do_connect()

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    print('Running command!')
    trigger_button()
else:
    print('power on or hard reset')
    #comment this out to drop to repl for debuging.
    machine.deepsleep()

def trigger_button():
    url = 'http://%s:5000/api/device/%s' % (wemo_ip, plug_name)
    headers = {'Content-Type' : 'text/json; charset=utf-8'}
	data = '{state: toggle}'
	resp = urequests.post(url, data=data, headers=headers)
	print(resp.json())
	machine.deepsleep()
