import itertools
import numpy
import time

import pypot.dynamixel

AMP = 30
FREQ = 0.5

if __name__ == '__main__':
    ports = pypot.dynamixel.get_available_ports()
    print('available ports:', ports)

    if not ports:
        raise IOError('No port available.')

    port = ports[0]
    print('Using the first on the list', port)

    dxl_io = pypot.dynamixel.DxlIO(port)
    print('Connected!')

    # dxl_io.factory_reset()
    # print("reset !")
    # exit(0)

    found_ids = dxl_io.scan()
    print('Found ids:', found_ids)

    if len(found_ids) < 2:
        raise IOError('You should connect at least two motors on the bus for this test.')

    ids = found_ids[:2]

    dxl_io.enable_torque(ids)


d=int(input("entrer une distance"))


dxl_io1 = pypot.dynamixel.DxlIO(ports[0])
dxl_io1.set_wheel_mode([1])
dxl_io1.set_moving_speed({1: 10})
dxl_io1.set_goal_position(d)

dxl_io2 = pypot.dynamixel.DxlIO(ports[1])
dxl_io2.set_wheel_mode([1])
dxl_io2.set_moving_speed({1: 10})
dxl_io2.set_goal_position(d)