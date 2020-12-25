from turtle import *
from random import *
import time

reset()

s = 0

points = 0

wining_text = ["You Won", "Good Job", "Your a Pro at this"]
lossing_text = ["Better Luck next time", "BOOOOOOOOOO", "Its ok to Loss"]

info = Turtle()
info.penup()
info.hideturtle()
info.goto(-180, 160)
info.color('blue')
info.write(points, font=('Arial', 20, 'bold'))

info_2 = Turtle()
info_2.penup()
info_2.hideturtle()
info_2.goto(-50, 300)
info_2.color('blue')

info_3 = Turtle()
info_3.penup()
info_3.hideturtle()
info_3.goto(-200, 200)
info_3.color('blue')
info_3.write("high is slow a to d speed: 0", font=('Arial', 20, 'bold'))
screen = getscreen()

guy = Turtle()
guy.color('green')
guy.shape('square')

tryy = 0

penup()
hideturtle()
speed(0)


def catch(x, y):
    goto(x, y)

    global tryy
    global points

    if points != 3 and tryy != 5:
        if distance(guy.pos()) < 10 and points != 3 and tryy != 5:
            color('red')
            points = points + 1
            info.clear()
            info.write(points, font=('Arial', 20, 'bold'))
        else:
            tryy = tryy + 1
            color('black')
        dot(20)


def add():
    global s
    s = s + 0.5
    info_3.clear()
    info_3.write("high is slow a to d speed: {}".format(s), font=('Arial', 20, 'bold'))


def minus():
    global s
    s = s - 0.5
    info_3.clear()
    info_3.write("high is slow a to d speed: {}".format(s), font=('Arial', 20, 'bold'))


def move():
    info_3.clear()
    for n in range(100):
        if points == 3 or tryy == 5:
            if points == 3:
                info_2.write(choice(wining_text), font=('Arial', 20, 'bold'))

            elif tryy == 5:
                info_2.write(choice(lossing_text), font=('Arial', 20, 'bold'))
            break
        x = randint(-200, 200)
        y = randint(-200, 200)
        guy.penup()
        guy.clear()
        guy.goto(x, y)
        time.sleep(s)


screen.onclick(catch)
screen.listen()
screen.onkeypress(add, "d")
screen.onkeypress(minus, "a")
screen.onkeypress(move, "f")


while True:

    screen.update()
