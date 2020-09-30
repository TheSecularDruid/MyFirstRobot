import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()
if not ports:
    exit('No port')

dxl_io = pypot.dynamixel.DxlIO(ports[1])
dxl_io.set_wheel_mode([1])
 t0 = time.time()
    while True:
        t = time.time()
        if (t - t0) > 5:
            break

        dxl_io.set_moving_speed({1: 10})

        time.sleep(5)
