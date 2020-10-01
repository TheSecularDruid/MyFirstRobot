import cv2 as cv
import time
import numpy as np


def openCamera():
    cam = cv.videoCapture(-1)
    if(not cam.isOpened()):
        raise IOError
    return cam

def closeCamera(camera):
    camera.release()
    cv2.destroyAllWindows()
    
def displayVideo(camera, time_out=10):
    if(not camera.isOpened()):
        raise IOError

    time_init = time.time()
    while(time.time()-time_init<time_out):
        ret,frame = camera.read()
    
        if(!ret):
            raise IOError

        imshow(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
	    raise KeyboardInterrupt


def colorFilter(image, color): #returns binImage
    image = cv.GaussianBlur(image, (5,3))
    upper = [0,0,0]
    lower = [0,0,0]
    hsv = cvtColor(image, cv.COLOR_BGR2HSV)
    
    if(color='Yellow'):
        #setup lower and upper values to something adapted
    if(color='Blue'):
        #same
    if(color='Green'):
        #same
    if(color='Red'):
        #same

    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(image, image, mask)
    return result

def detectCrossing(binImage):
     #ToDo

def detectLineAngle(binImage):
    #ToDo

    
