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
import math

class Motor():
    def __init__(self):
        ports = pypot.dynamixel.get_available_ports()
        if not ports:
            exit('No port')
        self.dxl_io = pypot.dynamixel.DxlIO(ports[0])
        self.dxl_io.set_wheel_mode([1,2])

    def set_speed_left_wheels(self, speed):
        self.dxl_io.set_moving_speed({1: speed})
    
    def set_goal_position(self,position):
        self.dxl_io.set_goal_position({1:position})

    def set_speed_right_wheels(self, speed):
        self.dxl_io.set_moving_speed({2: speed})

    def get_speed_left_wheels(self):
        return self.dxl_io.get_present_speed([1])

    def get_speed_right_wheels(self):
        return self.dxl_io.get_present_speed([2])

    def acrossDistance(self,speed,distance):
        omega=speed*1.39*2*math.pi/60
        radiusWheel=0.026
        self.set_speed_left_wheels(speed)
        self.set_speed_right_wheels(-speed)
        time.sleep(distance/(0.14*speed*radiusWheel))
        self.set_speed_right_wheels(0)
        self.set_speed_left_wheels(0)

if __name__ == "__main__":
    m = Motor()
    # m.set_speed_left_wheels(60)
    # m.set_speed_right_wheels(-60)
    # time.sleep(10)
    # m.set_speed_left_wheels(60)
    # m.set_speed_right_wheels(-30)
    # time.sleep(10)
    # m.set_speed_right_wheels(0)
    # m.set_speed_left_wheels(0)
    # m.acrossDistance(50,3)
    set_goal_position(-90)
    print('test')

    print(m.get_speed_right_wheels())
