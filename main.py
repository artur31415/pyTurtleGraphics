import math
import string
import pygame
from random import *

import time

from mpmath import mp

from turtle_graphics import *

pygame.init()
pygame.font.init()

# seed random number generator
#seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 1440
height = 900

screen = pygame.display.set_mode([width, height])

ui_font = pygame.font.SysFont('Comic Sans MS', 14)

running = True

clock = pygame.time.Clock()

theta_ratio = 10
ds = width / 2

myTurtle = TurtleGraphics((width / 2, height / 2), theta_ratio, ds)

turtle_dirs = []

num_of_digits = 1000000

mp.prec = num_of_digits
mp.dps = num_of_digits  # set number of digits

turtle_number = mp.e #mp.pi #mp.mpf(1) / 119. # prime number

start_time = time.time()
total_time = 0
################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def get_digits(num, count):
    digits = [math.floor(num)]
    current_num = num - math.floor(num)
    for i in range(count - 1):
        digit = math.floor(current_num * 10.0)
        digits.append(digit)
        current_num = current_num * 10.0 - digit

    return digits
################################################################################################
#                                           MAIN LOOP
################################################################################################

turtle_dirs = get_digits(turtle_number, num_of_digits)

print("digits = ", str(turtle_dirs))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##################################################################
    # UPDATE CODE
    ##################################################################

    if myTurtle.num_of_steps < len(turtle_dirs):
        for i in range(10000):
            myTurtle.turn(turtle_dirs[myTurtle.num_of_steps])
            myTurtle.forward()

            last_p = myTurtle.get_scaled_pos(-1)
            ratio = 0
            if last_p[0] < 0 or last_p[1] < 0 or last_p[0] > width or last_p[1] > height:
                ratio = 0.1
                myTurtle.ds = myTurtle.ds * (1 - ratio)
                print("ds = ", myTurtle.ds)

    ##################################################################
    # DRAW CODE
    ##################################################################

    screen.fill((150, 150, 150))

    myTurtle.draw(screen)

    ui_str = ""

    if myTurtle.num_of_steps < len(turtle_dirs):
        if myTurtle.num_of_steps % 100 == 0:
            total_time = time.time() - start_time
            ui_str = "step " + str(myTurtle.num_of_steps) + "/" + str(num_of_digits) + " in " + str(total_time) + " seconds"
            
            #print("--- %s seconds ---" % (total_time))
            #print(ui_str)
    else:
        ui_str = "Complete " + str(myTurtle.num_of_steps) + " digits in " + str(total_time) + " seconds"
        

    textsurface = ui_font.render(ui_str, False, (255, 0, 0))
    screen.blit(textsurface, (0, 0))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(50)
    

# Done! Time to quit.
pygame.quit()