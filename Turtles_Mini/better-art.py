import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for side in range(3):
        some_turtle.forward(100)
        some_turtle.left(120)

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor("blue")

    chuck = turtle.Turtle()
    chuck.shape("classic")
    chuck.color("green")
    chuck.speed(10)
    for i in range(36):
        draw_triangle(chuck)
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
