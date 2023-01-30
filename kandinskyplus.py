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


def fill_line(x1, y1, x2, y2, color):
    dx = x2-x1
    dy = y2-y1
    if dx == 0:
        fill_rect(x1, y1, 1, dy, color)
    else:
        a = dy/dx
        b = -a*x1 + y1
        if abs(dx) < abs(dy):
            for x in range(int(x1*a), int(x2*a)):
                set_pixel(int(x/a), int(x + b), color)
        else:
            for x in range(x1, x2):
                set_pixel(x, int(a*x + b), color)
