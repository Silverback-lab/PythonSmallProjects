from __future__ import division
import autopy
import time

x0, y0 = 800, 300
xf, yf = 100, 600

total_time = 5.00  # in seconds
draw_steps = 1000  # total times to update cursor

dx = (xf-x0)/draw_steps
dy = (yf-y0)/draw_steps
dt = total_time/draw_steps

for n in xrange(draw_steps):
    x = int(x0+dx*n)
    y = int(y0+dy*n)
    autopy.mouse.move(x,y)
    time.sleep(dt)