import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
print('available ports:', ports)
port=int(input("Choisissez le port"))

dxl_io = pypot.dynamixel.DxlIO(port)
dxl_io.set_wheel_mode([1])
t0 = time.time()
while True:
    t = time.time()
    if (t - t0) > 5:
        break

    dxl_io.set_moving_speed({1: 10})

    time.sleep(5)
