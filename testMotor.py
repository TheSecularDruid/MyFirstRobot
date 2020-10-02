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
import matplotlib.pyplot as plt
import Odometry as odom

speed=50
radiusWheel=26
entraxe=89
omegaL=speed*1.39*2*math.pi/60
omegaR=speed*1.39*2*math.pi/60
vitesseL=radiusWheel*omegaL
vitesseR=radiusWheel*omegaR
vitesseT=vitesseR


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
        radiusWheel=26
        self.set_speed_left_wheels(speed)
        self.set_speed_right_wheels(-speed)
        time.sleep(distance/(0.14*speed*radiusWheel))
        self.set_speed_right_wheels(0)
        self.set_speed_left_wheels(0)
    
    def getStateWheel(self):
        speedL=self.get_speed_left_wheels()
        speedR=self.get_speed_right_wheels()
        if  (speedL[0]!=0 or speedR[0]!=0):
            print("les moteurs sont mobiles")
            return 1
        else:
            print("les moteurs sont immobiles")
            return 0 


    def go_to_xyteta(self,x,y,teta):
        tetaRad=teta*math.pi/180
        self.set_speed_left_wheels(speed)
        self.set_speed_right_wheels(-speed)
        time.sleep(x/(vitesseT))
        if (y>=0):
            self.set_speed_left_wheels(speed)
            self.set_speed_right_wheels(0)
            time.sleep(2*entraxe*math.pi/(2*vitesseL))
            self.set_speed_left_wheels(speed)
            self.set_speed_right_wheels(-speed)
            time.sleep(y/(vitesseT))

        else:
            self.set_speed_left_wheels(0)
            self.set_speed_right_wheels(-speed)
            time.sleep(2*entraxe*math.pi/(2*vitesseR))  
            self.set_speed_left_wheels(speed)
            self.set_speed_right_wheels(-speed)
            time.sleep(abs(y)/(vitesseT))
        if teta>=0:
            self.set_speed_left_wheels(0)
            self.set_speed_right_wheels(-speed)
            time.sleep(2*entraxe*tetaRad/(vitesseL))
        else:    
            self.set_speed_left_wheels(speed)
            self.set_speed_right_wheels(0)
            time.sleep(2*entraxe*abs(tetaRad)/(vitesseL))

        self.set_speed_left_wheels(0)
        self.set_speed_right_wheels(0)


        #     self.set_speed_left_wheels(speed)
        #     self.set_speed_right_wheels(-speed)
        #     time.sleep(y/vitesseT)
        #     self.set_speed_left_wheels(0)
        #     self.set_speed_right_wheels(-speed)
        #     time.sleep(2*entraxe*tetaRad/(vitesseL))
        #     self.set_speed_left_wheels(0)
        #     self.set_speed_right_wheels(0)

        #     self.set_speed_left_wheels(0)
        #     self.set_speed_right_wheels(-speed)
        #     time.sleep(2*entraxe*tetaRad/(vitesseR))
        #     self.set_speed_left_wheels(speed)
        #     self.set_speed_right_wheels(-speed)
        #     time.sleep(math.sqrt(x**2+y**2)/vitesseT)
        #     self.set_speed_left_wheels(0)
        #     self.set_speed_right_wheels(0)
        # else:
        #     self.set_speed_left_wheels(speed)
        #     self.set_speed_right_wheels(0)
        #     time.sleep(2*entraxe*abs(tetaRad)/(vitesseL))
        #     self.set_speed_left_wheels(speed)
        #     self.set_speed_right_wheels(-speed)
        #     time.sleep(math.sqrt(x**2+y**2)/vitesseT)
        #     self.set_speed_left_wheels(0)
        #     self.set_speed_right_wheels(0)
    
    
    
    def odometryPlot(self,deltaT):  
        tetai=0
        xi=0
        yi=0
        t=0
        # while self.getStateWheel()==1:
        while True:
            speedR=self.get_speed_right_wheels()
            speedL=self.get_speed_left_wheels()
            l=odom.direct_kinematics(speedL[0],speedR[0])
            vLinear=l[0]
            vAngular=l[1]
            dx_dy_dteta=odom.odomWorld(vLinear,vAngular,deltaT,tetai)
            L=odom.tick_odom(xi,yi,tetai,dx_dy_dteta)
            xi=L[0]
            yi=L[1]
            tetai=L[2]
            time.sleep(deltaT)
            return (xi,yi)
            




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
    m.go_to_xyteta(1000,1000,60)
    X=[0]
    Y=[0]
   
    while m.getStateWheel()==1:
        print('test')
        L=m.odometryPlot(0.1)
        X.append(L[0])
        Y.append(L[0])
        
    print(X)
    plt.plot(X,Y)    
    plt.show()
    
    
    



    # print(m.get_speed_right_wheels())
