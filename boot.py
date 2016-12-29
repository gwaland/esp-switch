# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

from config import *
import esp
from flashbdev import bdev
import machine

ADC_MODE_VCC = 255
ADC_MODE_ADC = 0

def set_adc_mode(mode):
    sector_size = bdev.SEC_SIZE
    flash_size = esp.flash_size() # device dependent
    init_sector = int(flash_size / sector_size - 4)
    data = bytearray(esp.flash_read(init_sector * sector_size, sector_size))
    if data[107] == mode:
        return  # flash is already correct; nothing to do
    else:
        data[107] = mode  # re-write flash
        esp.flash_erase(init_sector)
        esp.flash_write(init_sector * sector_size, data)
        print("ADC mode changed in flash; restart to use it!")
        machine.reset()

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

set_adc_mode(ADC_MODE_VCC)
