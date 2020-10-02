import cv2 as cv
import time
import numpy as np


def openCamera():
    cam = cv.VideoCapture(-1)
    if(not cam.isOpened()):
        raise IOError
    cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv.CAP_PROP_FPS,1)
    return cam

def closeCamera(camera):
    camera.release()
    cv.destroyAllWindows()

def displayVideo(camera, time_out=10):
    if(not camera.isOpened()):
        raise IOError

    time_init = time.time()
    while(time.time()-time_init<time_out):
        ret,frame = camera.read()

        if(not ret):
            raise IOError

        imshow(frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            raise KeyboardInterrupt


def colorFilter(image, color): #returns binImage
    image = cv.GaussianBlur(image, (5,5),5)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    if(color=='Green'):
        lower = np.array([50,50,150])
        upper = np.array([100, 100, 190])

    elif(color=='Red'):
        lower = np.array([0,100,100])
        upper = np.array([180,150,180])

    elif(color=='Blue'):
        lower = np.array([100,110,170])
        upper = np.array([130,160,230])

    elif(color=='Yellow'):
        lower = np.array([10,80,130])
        upper = np.array([50,180,255])

    else:
        print('the selected color is not supported')
        print('supported colors : Green, Red, Blue, Yellow')
        raise ValueError


    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(image, image, mask=mask)
    return result[:,:,2]

def detectCrossing(binImage):
     #ToDo
     pass

def detectLineCenter(binImage):
    contours, _ = cv.findContours(binImage, 1, cv.CHAIN_APPROX_SIMPLE)
    if(np.shape(contours)[0]!=0):

        c = max(contours, key=cv.contourArea)
        M = cv.moments(c)
        center = np.array([int(M['m10']/M['m00']),int(M['m01']/M['m00'])])
        return center
    return 0

def pixelToRobot(pixel,offset_cam, window_size,cam):
    x_rob = offset_cam[0] - window_size[0]*pixel[0]/cam.get(cv.CAP_PROP_FRAME_HEIGHT)
    y_rob = offset_cam[1] - window_size[1]*pixel[1]/cam.get(cv.CAP_PROP_FRAME_WIDTH)
    return (x_rob,y_rob)

#test calls
if __name__=='__main__':
    cam = openCamera()

    while(True):
        ret, frame = cam.read()
        if(not ret):
            print("image not fetched by camera")
            raise IOError
        #detectLineAngle(colorFilter(frame,'Yellow'))
    
        cv.imshow("Seen image",frame)
        cv.waitKey(1)
    closeCamera(cam)
'''
        cv.imshow('Green filter',colorFilter(frame,'Green'))
        cv.imshow("Yellow filter",colorFilter(frame,'Yellow'))
        cv.imshow('Blue filter',colorFilter(frame,'Blue'))
        cv.imshow('Red filter',colorFilter(frame,'Red'))
        cv.waitKey(1)
'''     
    
