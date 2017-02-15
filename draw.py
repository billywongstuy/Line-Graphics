from __future__ import division
from display import *

# Bresenham algorithm
# Works only for octant 1

def lineO1( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0

    A = y1-y0
    B = -(x1-x0)

    d = 2*A + B

    while x < x1:
        plot(screen,color,x,y)
        x+=1
        if d > 0:
            y+=1
            d+= 2*B
        d += 2*A


# x+1/2, y+1
def lineO2(screen,x0,y0,x1,y1,color):
    x = x0
    y = y0

    A = y1-y0
    B = -(x1-x0)
    
    d = A+2*B
    
    while y <= y1:
        plot(screen,color,x,y)
	y += 1
	if d < 0:
	    x += 1
	    d += 2*A
	d += 2*B


# x+1/2 , y-1
def lineO7(screen,x0,y0,x1,y1,color):
    x = x0
    y = y0

    A = y1-y0
    B = -(x1-x0)

    d = A-2*B

    while y > y1:
        plot(screen,color,x,y)
        y -= 1
        d -= 2*B
        if d > 0:
            x+=1
            d += 2*A

# x+1, y-1/2
def lineO8(screen,x0,y0,x1,y1,color):
    x = x0
    y = y0

    A = y1-y0
    B = -(x1-x0)

    d = 2*A-B

    while x < x1:
        plot(screen,color,x,y)
        x += 1
        d += 2*A
        if d < 0:
            y-=1
            d -= 2*B


def draw_line( screen, x0, y0, x1, y1, color ):
    if x0 > x1:
        tempX = x0
        tempY = y0
        x0 = x1
        y0 = y1
        x1 = tempX
        y1 = tempY


    if x0 == x1:
        slope = "Infinite"     
    else:
        slope = (y1-y0)/(x1-x0)

        
    if slope == "Infinite":
        while y0 <= y1:
            plot(screen,color,x0,y0)
            y0+=1
    elif slope > 0 and slope < 1:
        lineO1(screen,x0,y0,x1,y1,color)
    elif slope > 1:
        lineO2(screen,x0,y0,x1,y1,color)
    elif slope < 0 and slope > -1:
        lineO8(screen,x0,y0,x1,y1,color)
    elif slope < -1:
        lineO7(screen,x0,y0,x1,y1,color)
    else:
        pass #ERROR

    
