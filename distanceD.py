import itertools
import numpy
import time

import pypot.dynamixel

AMP = 30
FREQ = 0.5

if __name__ == '__main__':
    ports = pypot.dynamixel.get_available_ports()
    print('available ports:', ports)







d=int(input("entrer une distance"))


t0 = time.time()
while True:
    t = time.time()
    if (t - t0) > 5:
        break
    dxl_io1 = pypot.dynamixel.DxlIO(ports[0])
    dxl_io1.set_wheel_mode([1])
    dxl_io1.set_moving_speed({1: 40})
    dxl_io1.set_goal_position(d)

    dxl_io2 = pypot.dynamixel.DxlIO(ports[1])
    dxl_io2.set_wheel_mode([1])
    dxl_io2.set_moving_speed({1: 40})
    dxl_io2.set_goal_position(d)
    time.sleep(0.2)