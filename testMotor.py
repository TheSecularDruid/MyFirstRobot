import pypot.dynamixel
import time

# ports = pypot.dynamixel.get_available_ports()
# print('available ports:', ports)


dxl_io = pypot.dynamixel.DxlIO(ports[0])
dxl_io.set_wheel_mode([1,2])
dxl_io.set_moving_speed({2: 40})

# found_ids = dxl_io.scan(range(10))
# print('Found ids:', found_ids)
# t0 = time.time()
# while True:
#     t = time.time()
#     if (t - t0) > 5:
#         break

#     dxl_io.set_moving_speed({2: 40})

    

#     time.sleep(5)
