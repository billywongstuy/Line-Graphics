from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]


'''
display(screen)
save_extension(screen, 'img.png')

'''

#Don't call display_name and save_extension while the image is open

x0 = 0
y0 = 0
x1 = 500

for y1 in range(0,500,10):
    color[0] += random.randint(0,255)
    color[1] += random.randint(0,255)
    color[2] += random.randint(0,255)
    color[0] = color[0]%256
    color[1] = color[1]%256
    color[2] = color[2]%256
    
    draw_line(screen,x0,y0,x1,y1,color)

save_extension(screen, 'img.png')
display(screen)

'''
clear_screen(screen)

for y1 in range(0,500,10):
    color[0] += random.randint(0,255)
    color[1] += random.randint(0,255)
    color[2] += random.randint(0,255)
    color[0] = color[0]%256
    color[1] = color[1]%256
    color[2] = color[2]%256
    
    draw_line_own(screen,x0,y0,x1,y1,color)
    
save_extension(screen, 'imgme.png')
display_name(screen,'imgme.ppm')

'''
