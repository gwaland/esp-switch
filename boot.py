# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

#import webrepl
import config.py
#ssid='ssid'
#ssid_pass='password'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, ssid_pass)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#webrepl.start()
