import serial

'''
ser.in_waiting # что в буфере
ser.write(b'b')  # отправляем последовательность байт
ser.write(b'1')  # смотрим 1 сенсор
data = ser.read_all().decode().strip()
'''

mesg_length = {b'1': 5,
               b'2': 5}  # и первый, и второй сенсор могут отправить до 5 байт


def get_connection():
    ser = serial.Serial('COM6', timeout=1)  # в путь пишем порт ардуино
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


ser = get_connection()
for i in range(10):
    print(f'Data are (try {i})', get_sensor(ser, b'1'))
ser.close()
ser = get_connection()
for i in range(10, 20):
    print(f'Data are (try {i})', get_sensor(ser, b'2'))
ser.close()
