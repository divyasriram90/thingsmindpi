from pubnub import Pubnub
from gpiozero import LED
from time import sleep
import subprocess

pubnub = Pubnub(
    publish_key = "pub-c-5b4ed4d3-8921-45cb-8151-d48aaebb2467",
    subscribe_key = "sub-c-f7b16a98-a291-11e6-a1b1-0619f8945a4f")

led = LED(17)
channel = "manage"

def callback(message, channel):
    print('[' + channel + ']: ' + str(message))

    if message == 'install':
        print('install')
        subprocess.call('./install.sh')
    elif message == 'reboot':
        print('reboot')
        subprocess.call('./reboot.sh')
    elif message == 'ledon':
        print('ledon')
        led.on()
        sleep(5)
        led.off()

pubnub.subscribe( channel, callback = callback)