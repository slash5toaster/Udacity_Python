import turtle

def draw_square():
    #get mah window
    window = turtle.Screen()
    window.bgcolor("red")

    chuck = turtle.Turtle()

    for side in range(4):
        chuck.forward(100)
        chuck.right(90)
        print side

    window.exitonclick()
#-------------

draw_square()
