import turtle
import time
# import random

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Functions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    y = head.ycor()
    x = head.xcor()

    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)

    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()