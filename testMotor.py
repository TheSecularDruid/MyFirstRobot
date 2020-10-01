import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
if not ports:
    exit('No port')

dxl_io_g = pypot.dynamixel.DxlIO(ports[0])
dxl_io_d = pypot.dynamixel.DxlIO(ports[1])
dxl_io_g.set_wheel_mode([1])
dxl_io_d.set_wheel_mode([1])
t0 = time.time()
while True:
    t = time.time()
    if (t - t0) > 5:
        break

    dxl_io_g.set_moving_speed({1: 10})
    dxl_io_d.set_moving_speed({1: 40})

    time.sleep(0.02)
