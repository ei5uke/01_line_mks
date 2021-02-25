from display import *
from draw import *
import random

s = new_screen()
c = [ 0, 255, 0 ]

"""
#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c) 
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4
c[BLUE] = 255;
draw_line(0, YRES-1, XRES-1, 0, s, c)
draw_line(0, YRES-1, XRES-1, YRES/2, s, c)
draw_line(XRES-1, 0, 0, YRES/2, s, c)

#octants 2 and 6
c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(0, 0, XRES/2, YRES-1, s, c)
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c)

#octants 7 and 3
c[BLUE] = 255
draw_line(0, YRES-1, XRES/2, 0, s, c)
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c)

#horizontal and vertical
c[BLUE] = 0
c[GREEN] = 255
draw_line(0, YRES/2, XRES-1, YRES/2, s, c)
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c)
"""#test code

#my drawing
c[RED] = 255
#c[GREEN] = 255
#c[BLUE] = 255
"""
draw_line(0, 499, 500, 499, s, c) 
draw_line(0, 375, 500, 375, s, c) 
draw_line(0, 250, 500, 250, s, c) 
draw_line(0, 125, 500, 125, s, c)
draw_line(0, 0, 500, 0, s, c)"""
for i in range (0, 20):
    for j in range(0, 20):
        x = random.randint(432, 437)
        y = random.randint(69, 74)
        z = random.randint(0, 250)
        c[RED] = random.randint(0, 255)
        c[GREEN] = random.randint(0, 255)
        c[BLUE] = random.randint(0, 255)
        draw_line(i * y, j * x, y, j * z, s, c)
        draw_line(j * y, i * z, j * z, x, s, c)    

display(s)
save_ppm(s, 'yarn.ppm')
"""
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')"""