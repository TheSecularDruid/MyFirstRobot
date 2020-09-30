import math
centerDistanceWheel=178
radiusWheel=25


def forward_kinematics()

def direct_kinematics(vgauche,vdroite)

def rotation(x0,y0):
    w=math.atanh(x0/y0)
    nbrWheelturn=(distanceWheel*w)/(4*radiusWheel)
    return nbrWheelturn

def newPosTrans(d,x0,y0,alpha0)
    x=d*cos(alpha0)+x0
    y=d*sin(alpha0)+y0
    alpha=alpha0
    return(x,y,alpha)


def newPosRotG(x0,y0,alpha0)
    alphaR=1/2*e
    x=x0-e*sin(alpha0)+e*sin(alpha0+alphaR)
    y=y0+e*cos(alpha0)-e*cos(alpha0+alphaR)
    alpha=alpha0+alphaR
    return(x,y,alpha)

def newPosRotD(x0,y0,alpha0)
    alphaR=1/2*e
    x=x0+e*sin(alpha0)-e*sin(alpha0-alphaR)
    y=y0-e*cos(alpha0)+e*cos(alpha0-alphaR)
    alpha=alpha0-alphaR
    return(x,y,alpha)



