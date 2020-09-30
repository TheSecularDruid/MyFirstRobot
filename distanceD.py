import pypot.dynamixel



d=int(input("entrer une distance"))
ports = pypot.dynamixel.get_available_ports()
if not ports:
    exit('No port')

dxl_io1 = pypot.dynamixel.DxlIO(ports[1])
dxl_io1.set_wheel_mode([1])
dxl_io1.set_moving_speed({1: 10})
dxl_io1.set_goal_position(d)

dxl_io2 = pypot.dynamixel.DxlIO(ports[2])
dxl_io2.set_wheel_mode([1])
dxl_io2.set_moving_speed({1: 10})
dxl_io2.set_goal_position(d)