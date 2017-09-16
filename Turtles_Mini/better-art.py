import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for side in range(3):
        some_turtle.forward(100)
        some_turtle.left(120)


def draw_diamond(some_turtle,angle1):
    # angle1 = 140
    angle2 = 180 - angle1
    for side in range(2):
        some_turtle.forward(100)
        some_turtle.right(angle1)
        some_turtle.forward(100)
        some_turtle.right(angle2)

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor("blue")

    chuck = turtle.Turtle()
    chuck.shape("classic")
    chuck.color("green")
    chuck.speed(20)
    # draw the flower
    chuck.right(90)
    chuck.forward(200)
    chuck.right(180)
    chuck.forward(200)
    for i in range(36):
        draw_diamond(chuck,160)
        chuck.left(10)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.speed(2)
    # angie.circle(100)
    #
    # ted = turtle.Turtle()
    # ted.shape("circle")
    # ted.color("purple")
    # ted.speed(2)
    # draw_triangle(ted)

    window.exitonclick()

draw_stuff()
