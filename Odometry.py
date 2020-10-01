import math
e=89
radiusWheel=25
         
distanceD = 0           #distance parcourue par la roue droite
distanceG = 0           #distance parcourue par la roue gauche
byte etatD             #état du capteur de roue droit
byte etatG             #état du capteur de roue gauche

tetaR-W=0 #angle entre repère robot et monde (initialement confondu)






def forward_kinematics()

def direct_kinematics(vleft,vright):
    vLinear=(vleft+vright)/2
    vAngular=(vleft-vright)/2*e
    return(vLinear,vAngular)

def inverse_kinematics(vLinear,vAngular):
    vleft=(vLinear+vAngular*e)
    vright=(vLinear-vAngular*e)
    return(vleft,vright)


def odomRobot(vLinear,vAngular,deltaT):
    dx=vLinear*deltaT
    dy=0
    dteta=vAngular*deltaT
    return[dx,dy,dteta]

def odomWorld(vLinear,vAngular,deltaT):
    dteta=vAngular*deltaT
    dx=math.cos(tetaR-W)*vLinear*deltaT
    dy=math.sin(tetaR-W)*vLinear*dteta*deltaT
    return(dx,dy,dteta)



def rotation(x0,y0):
    w=math.atanh(x0/y0)
    nbrWheelturn=(distanceWheel*w)/(4*radiusWheel)
    return nbrWheelturn

def newPosTrans(d,x0,y0,teta0):
    x=d*cos(teta0)+x0
    y=d*sin(teta0)+y0
    teta=teta0
    return(x,y,teta)


def newPosRotL(x0,y0,teta0):
    tetaR=vAngular*deltaT
    x=x0-e*sin(teta0)+e*sin(teta0+tetaR)
    y=y0+e*cos(teta0)-e*cos(teta0+tetaR)
    teta=teta0+tetaR
    return(x,y,teta)

def newPosRotR(x0,y0,teta0):
    tetaR=vAngular*deltaT
    x=x0+e*math.sin(teta0)-e*math.sin(teta0-tetaR)
    y=y0-e*cos(teta0)+e*cos(teta0-tetaR)
    teta=teta0-tetaR
    return(x,y,teta)


def tick_odom(xi,yi,tetai):
    dx_dy_dteta=odomWorld(vLinear,vAngular,deltaT)
    xf=xi+dx_dy_dteta[0]
    yf=yi+dx_dy_dteta[1]
    tetaf=tetaii+dx_dy_dteta[2]
    return [xf,yf,tetaf]

def go_to_xyteta(x,y,teta):
    
    

    




