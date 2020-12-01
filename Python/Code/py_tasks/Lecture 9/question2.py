import turtle

wn = turtle.Screen()
ben = turtle.Turtle()

def draw_square(object):
    object.right(90)
    object.backward(100)
    object.right(90)
    object.forward(100)
    object.right(90)
    object.backward(100)
    object.right(90)
    object.forward(100)

def draw_hexagon(object):
    for i in range(6):
        object.forward(90)
        object.left(300)

draw_square(ben)
draw_hexagon(ben)
