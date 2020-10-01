import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
print('available ports:', ports)


dxl_io = pypot.dynamixel.DxlIO(ports[0])
dxl_io.set_wheel_mode([1])
t0 = time.time()
while True:
    t = time.time()
    if (t - t0) > 5:
        break

    dxl_io.set_moving_speed({1: 40})
    dxl_io.set_moving_speed({0: 10})

    time.sleep(5)
