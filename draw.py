from display import *

#Returns a list with slope and y-intercept 
#adjusted so that the line works with ppm file writing
def equation4Pic(x0,y0,x1,y1):
    data = []
    data.append( ( (y1-y0) *1.0) /(x1-x0))
    data.append(y0-x0*data[0])
    return data

def onEquat(l,x,y):
    actY = l[0]*x+l[1]
    if actY == 0:
        return y == 0
    diff = abs(actY-y)*100/actY
    return diff < 0.5


# My own line equation
# Works for any line
# Not too efficient
def draw_line_own( screen, x0, y0, x1, y1, color ):
    es = equation4Pic(x0,y0,x1,y1)
    
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            if onEquat(es,x,y):
                plot(screen,color,x,len(screen)-y)
    

# Bresenham algorithm
# Works only for octant 1

def draw_line_bres( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    es = equation4Pic(x0,y0,x1,y1)
    A = es[0]
    B = -1
    d = 2*A + B
    pts = []
    while x <= x1:
        plot(screen,color,x,len(screen)-y)
        x+=1
        if d > 0:
            y+=1
            d+= 2*B
        d += 2*A
        
