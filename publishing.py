import paho.mqtt.client as paho
import serial

mesg_length = {b'1': 5, b'2': 5}


def get_connection():
    ser = serial.Serial('COM6', timeout=1) # вместо COM6, конечно, ваш порт
    return ser


def get_sensor(ser, sensor_byte, tries=3):
    for _ in range(tries):
        ser.write(sensor_byte)
        data = ser.read(mesg_length[sensor_byte]).decode().strip()
        if data == '':
            print('No data, something wrong')
        else:
            break
    return data


broker = "broker.hivemq.com"
client = paho.Client("kto-chto-228")

print('Connecting to broker', broker)
client.connect(broker)
client.loop_start()
print('Publishing')

for _ in range(10):
    ser = get_connection()
    for i in range(10):
        client.publish("house/bulb1", get_sensor(ser, b'1'))
    ser.close()
    ser = get_connection()
    for i in range(10, 20):
        client.publish("house/bulb1", get_sensor(ser, b'2'))
    ser.close()


client.disconnect()
client.loop_stop()
