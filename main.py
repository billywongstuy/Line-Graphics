from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]



#Don't call display_name and save_extension while the image is open


x0 = 250
y0 = 250


# Octants 1,4,5,8

#end x, start y, end y
smallM = [[500,250,500],[0,250,500],[0,0,250],[500,0,250]]

for case in smallM:
    for y1 in range(case[1],case[2],10):
        color[0] += random.randint(0,255)
        color[1] += random.randint(0,255)
        color[2] += random.randint(0,255)
        color[0] = color[0]%256
        color[1] = color[1]%256
        color[2] = color[2]%256
    
        draw_line(screen,x0,y0,case[0],y1,color)

#Octants 2,3,6,7

#end y, start x, end x        
bigM = [[500,250,500],[500,0,250],[0,0,250],[0,250,500]]


for case in bigM:
    for x1 in range(case[1],case[2],10):
        color[0] += random.randint(0,255)
        color[1] += random.randint(0,255)
        color[2] += random.randint(0,255)
        color[0] = color[0]%256
        color[1] = color[1]%256
        color[2] = color[2]%256
    
        draw_line(screen,x0,y0,x1,case[0],color)

save_extension(screen, 'img.png')
display(screen)
