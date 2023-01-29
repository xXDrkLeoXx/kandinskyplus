'''
TODO: fill_line(x1, y1, x2, y2)
TODO: fill_triangle(x1, y1, x2, y2, x3, y3)
TODO: optimized fill_circle algorithm with the inside square method
'''

from kandinsky import *


def fill_circle(xc, yc, radius, color):
    radcare = radius**2
    for y in range(yc-radius, yc+radius):
        dycare = (y-yc)**2
        for x in range(xc-radius, xc+radius):
            if ((x-xc)**2 + dycare) <= radcare:
                set_pixel(x, y, color)


circol = color(0, 0, 0)

fill_circle(160, 120, 50, circol)
