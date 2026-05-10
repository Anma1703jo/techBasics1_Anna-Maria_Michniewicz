#I hope it works. if not, I sent you a mail about it.

from turtle import *
import random

width = 400
height = 500

Screen().bgcolor('black')

speed(0)

colors = ['red', 'magenta', 'cyan', 'blue', 'violet', 'yellow', 'orange', 'purple', 'navy', 'turquoise', 'white']
random_color = random.choice(colors)


def random_color():
    return random.choice(colors)


x_start = -150
y_start = 150

for row in range(4):

    for column in range(4):
        penup()
        goto(x_start + column * 100, y_start - row * 100)
        pendown()

        for i in range(12):
            if row % 2 == 0 and column % 2 == 0:
                color(random_color())
            elif row % 2 == 0:
                color('yellow')
            elif column % 2 == 0:
                color('cyan')
            else:
                color(random_color())
            circle(30)
            right(30)

done()
