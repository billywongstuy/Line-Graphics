from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


'''
display(screen)
save_extension(screen, 'img.png')

'''

#Don't call display_name and save_extension while
#the image is open

x0 = 203
y0 = 80
x1 = 250
y1 = 400

draw_line_bres(screen,x0,y0,x1,y1,color)
save_extension(screen, 'imgbres.png')
display_name(screen,'imgbres.ppm')

clear_screen(screen)

draw_line_own(screen,x0,y0,x1,y1,color)
save_extension(screen, 'imgme.png')
display_name(screen,'imgme.ppm')
