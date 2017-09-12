import turtle

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor("red")

    chuck = turtle.Turtle()
    chuck.shape("classic")
    chuck.color("green")
    chuck.speed(2)

    for side in range(4):
        chuck.forward(100)
        chuck.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)

    ted = turtle.Turtle()
    ted.shape("arrow")
    ted.color("purple")
    ted.speed(2)
    for side in range(3):
        ted.forward(100)
        ted.left(120)

    window.exitonclick()

draw_stuff()
