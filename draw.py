from display import *
    

# Bresenham algorithm
# Works only for octant 1

def draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0

    A = y1-y0
    B = -(x1-x0)

    d = 2*A + B

    while x <= x1:
        plot(screen,color,x,len(screen)-y)
        x+=1
        if d > 0:
            y+=1
            d+= 2*B
        d += 2*A
        

#----------------------------------------------

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
# Works pretty bad for lines with slopes close to 0

def draw_line_own( screen, x0, y0, x1, y1, color ):
    es = equation4Pic(x0,y0,x1,y1)
    
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            if onEquat(es,x,y):
                plot(screen,color,x,len(screen)-y)
