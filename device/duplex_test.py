import serial
import time
import struct
dev = serial.Serial('/dev/ttyACM0', 9600)

n_wf = 0
n_all = 0
#print(ser.in_waiting)

def rt_process(entry):
    print(entry)
    
while True:
    dev.read_until('!'.encode())
    res = dev.read_until('@'.encode())
    n_all += 1
    if not len(res) == 35:  # 34+1
        continue
    n_wf += 1
    rt_process(struct.unpack_from('<fffffffhhh', res))
    n_wf += 1
    # print(time.time(), data)
    #ser.write(bytes([1]))
    # ser.flush()
    #time.sleep(0.5)



