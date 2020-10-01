# import pypot.dynamixel
# import time

# ports = pypot.dynamixel.get_available_ports()
# # print('available ports:', ports)


# dxl_io = pypot.dynamixel.DxlIO(ports[0])
# dxl_io.set_wheel_mode([1,2])
# dxl_io.set_moving_speed({2: 40})

# # found_ids = dxl_io.scan(range(10))
# # print('Found ids:', found_ids)
# # t0 = time.time()
# # while True:
# #     t = time.time()
# #     if (t - t0) > 5:
# #         break

# #     dxl_io.set_moving_speed({2: 40})

    

# #     time.sleep(5)

import pypot.dynamixel
import time

class Motor():
    def init(self):
        ports = pypot.dynamixel.get_available_ports()
        if not ports:
            exit('No port')
        self.dxl_io = pypot.dynamixel.DxlIO(ports[0])
        self.dxl_io.set_wheel_mode([1,2])

    def set_speed_left_wheels(self, speed):
        self.dxl_io.set_moving_speed({1: speed})

    def set_speed_right_wheels(self, speed):
        self.dxl_io.set_moving_speed({2: speed})

    def get_speed_left_wheels(self):
        return self.dxl_io.get_present_speed([1])

    def get_speed_right_wheels(self):
        return self.dxl_io.get_present_speed([2])

if __name__ == "main":
    m = Motor()
    m.set_speed_left_wheels(50)
    m.set_speed_right_wheels(50)
    time.sleep(2)
    m.set_speed_right_wheels(0)
    m.set_speed_left_wheels(0)
    print('test')

    print(m.get_speed_right_wheels())
