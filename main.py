from display import *
from draw import *
import random, math

screen = new_screen()
color = [ 0, 255, 0 ]



#Don't call display_name and save_extension while the image is open


x0 = 250
y0 = 250


# Octants 1,4,5,8

#end x, start y, end y
smallM = [[500,250,501],[0,250,501],[0,0,251],[500,0,251]]

for case in smallM:
    for y1 in range(case[1],case[2],10):
        color[0] += random.randint(0,255)
        color[1] += random.randint(0,255)
        color[2] += random.randint(0,255)
        color[0] = color[0]%256
        color[1] = color[1]%256
        color[2] = color[2]%256
    
        draw_line(screen,x0,y0,case[0],y1,color)

draw_line(screen,0,250,500,250,color)

#Octants 2,3,6,7

#end y, start x, end x        
bigM = [[500,250,501],[500,0,251],[0,0,251],[0,250,501]]


for case in bigM:
    for x1 in range(case[1],case[2],10):
        color[0] += random.randint(0,255)
        color[1] += random.randint(0,255)
        color[2] += random.randint(0,255)
        color[0] = color[0]%256
        color[1] = color[1]%256
        color[2] = color[2]%256
    
        draw_line(screen,x0,y0,x1,case[0],color)

draw_line(screen,250,0,250,500,color)

save_extension(screen, 'img.png')
display(screen)



'''


def calcSlope(x0,y0,x1,y1):
    if x0 == x1:
        return "Undefined"
    return (y1-y0)/(x1-x0)

def distPts(x0,y0,x1,y1):
    return math.sqrt(math.pow((x1-x0),2)+math.pow((y1-y0),2))


d = 2
topL = [0,500]
topR = [500,500]
botL = [0,0]
botR = [500,0]
prevTlAng = None
prevTrAng = None
prevBrAng = None
prevBlAng = None
prevTlSlope = 0
prevTrSlope = 0
prevBrSlope = 0
prevBlSlope = 0
firstThru = False

# d = 1
# d = 5 breaks after 0,61
# d = 10 breaks after 0,31
# d = 20 breaks after 0,16

for a in range(0,152):
    
    # TOP LEFT DROPPING
    if prevTlAng != None:
        oldTopL = topL[0]
        topL[0] += d*math.sin(prevTlAng)
        #topL[1] -= d*math.cos(prevTlAng)
        topL[1] = topL[1] + prevTlSlope*(topL[0]-oldTopL)
    else:
        topL[0] += d
    topDist = distPts(topL[0],topL[1],topR[0],topR[1])
    prevTlAng = math.atan((topDist-d)/d)
    
        
    # TOP RIGHT
    if prevTrAng != None:
        oldTopR = topR[1]
        #topR[0] -= d*math.cos(prevTrAng)
        topR[1] -= d*math.sin(prevTrAng)
        if prevTrSlope == 0:
            topR[0] = topR[0] - prevTrSlope*(oldTopR - topR[1])
        else:
            topR[0] = topR[0] - (1/prevTrSlope)*(oldTopR - topR[1])
            
    else:
        topR[1] -= d
    rtDist = distPts(botR[0],botR[1],topR[0],topR[1])
    prevTrAng = math.atan((rtDist-d)/d)
    
    

    # BOTTOM RIGHT
    if prevBrAng != None:
        oldBotR = botR[0]
        botR[0] -= d*math.sin(prevBrAng)
        #botR[1] += d*math.cos(prevBrAng)
        botR[1] = botR[1] + prevBrSlope*(botR[0]-oldBotR)
    else:
        botR[0] -= d
    btDist = distPts(botL[0],botL[1],botR[0],botR[1])
    prevBrAng = math.atan((btDist-d)/d)

    # BOTTOM LEFT
    if prevBlAng != None:
        oldBotL = botL[1]
        #botL[0] += d*math.cos(prevBrAng)
        botL[1] += d*math.sin(prevBrAng)
        if prevBlSlope == 0:
            botL[0] = botL[0] - prevBlSlope*(oldBotL - botL[1])
        else:
            botL[0] = botL[0] - (1/prevBlSlope)*(oldBotL - botL[1])
    else:
        botL[1] += d
    ltDist = distPts(botL[0],botL[1],topL[0],topL[1])
    prevBlAng = math.atan((ltDist-d)/d)

    # LINE
    draw_line(screen,int(topL[0]),int(topL[1]),int(topR[0]),int(topR[1]),color)
    draw_line(screen,int(topR[0]),int(topR[1]),int(botR[0]),int(botR[1]),color)
    draw_line(screen,int(botR[0]),int(botR[1]),int(botL[0]),int(botL[1]),color)
    draw_line(screen,int(botL[0]),int(botL[1]),int(topL[0]),int(topL[1]),color)

    # CHANGE COLOR
    
    color[0] += 34
    color[1] += 34
    color[2] += 34
    

    print [int(topL[0]),int(topL[1])],[int(topR[0]),int(topR[1])],[int(botR[0]),int(botR[1])],[int(botL[0]),int(botL[1])]


    if firstThru:
        prevTlSlope = calcSlope(topL[0],topL[1],topR[0],topR[1])
        prevTrSlope = calcSlope(botR[0],botR[1],topR[0],topR[1])
        prevBrSlope = calcSlope(botL[0],botL[1],botR[0],botR[1])
        prevBlSlope = calcSlope(botL[0],botL[1],topL[0],topL[1])

    firstThru = True
        
save_extension(screen, 'img.png')
#display(screen)
'''
