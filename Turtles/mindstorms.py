import turtle

# def make_window():
#     #get mah window
#     window = turtle.Screen()
#     window.bgcolor("red")
#     window.exitonclick()

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    chuck = turtle.Turtle()
    chuck.shape("classic")
    chuck.color("green")
    chuck.speed(2)

    for side in range(4):
        chuck.forward(100)
        chuck.right(90)
        # print side
    window.exitonclick()

#-------------
def draw_circle():
    window = turtle.Screen()
    window.bgcolor("green")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)

    window.exitonclick()
#-------------
def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("orange")

    ted = turtle.Turtle()
    ted.shape("arrow")
    ted.color("purple")
    ted.speed(2)
    for side in range(3):
        ted.forward(100)
        ted.left(120)

    window.exitonclick()

# make_window()
# draw_square()
# draw_circle()
draw_triangle()
