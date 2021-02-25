from display import *

def switch(x0, y0, x1, y1):
    a, b = int(y1 - y0), int(x1 - x0) #delta y, x
    if (b != 0):
        x2, y2, x3, y3 = int(min(x0,x1)), int(min(y0,y1)), int(max(x0,x1)), int(max(y0,y1))  
        if (a / b > 0): #return left point, right point, positive slope
            a, b = int(y3 - y2), int(x3 - x2)
            return x2, y2, x3, y3, a, b
        elif (a / b < 0): #return left point, right point, negative slope
            a, b = int(y2 - y3), int(x3 - x2)
            return x2, y3, x3, y2, a, b
    return int(x0), int(y0), int(x1), int(y1), a, b #return point0, point1
            
def draw_line( x0, y0, x1, y1, screen, color ):
    x, y, x1, y1, a, b = switch(x0, y0, x1, y1)
    if (b == 0): #vertical lines
        while (y < y1):
            plot(screen, color, x, y)
            y += 1
    elif (a == 0): #horizontal lines
        while (x < x1):
            plot(screen, color, x, y)
            x += 1
    elif (0 < (a / b) <= 1): #octant 1 and 5
        d = 2 * a - b
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * -b
            x += 1
            d += 2 * a
    elif (1 < (a / b)): #octant 2 and 6
        d = -a + 2 * b
        while (y <= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * -a
            y += 1
            d += 2 * b
    elif ((a / b) < -1): #octant 3 and 7
        d = a + 2 * b
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d -= 2 * -a
            y -= 1
            d += 2 * b
    else: #octant 4 and 8 
        d = 2 * a + b
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * -b
            x += 1
            d += 2 * a