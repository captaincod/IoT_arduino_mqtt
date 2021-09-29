import time
import serial
import paho.mqtt.client as paho
from paho.mqtt import subscribe

broker = 'broker.hivemq.com'
ser = serial.Serial('COM4', timeout=1) # вместо COM4 - ваш порт на ардуино


def on_message_print(client, userdata, message):
    print("received message = %s" % (message.payload.decode('utf-8')))
    if not message.payload.decode('utf-8').isdigit(): # если приняли строковое сообщение
        ser.write(b'd')
    elif int(message.payload.decode('utf-8')) > 400:  # когда мало света
        ser.write(b'u')
    else: # много света
        ser.write(b'd')

ser.write(b'd')

subscribe.callback(on_message_print, "house/bulb1", hostname="broker.hivemq.com")

client = paho.Client('kto-chto-229')
print('Connect to broker', broker)
client.connect(broker)
client.loop_start()
print('Subscribing')
client.subscribe('house/bulb1')
time.sleep(30)
client.disconnect()
client.loop_stop()
