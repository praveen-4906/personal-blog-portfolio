import turtle
pen = turtle.Turtle()
pen.getscreen().bgcolor("red")

pen.color("white")
pen.begin_fill()

pen.penup()
pen.right(90)
pen.forward(50)
pen.left(90+45)
pen.pendown()
pen.forward(100)
pen.circle(50,180)
pen.right(90)
pen.circle(50,180)
pen.forward(100)

pen.end_fill()

pen.left(90+45)
pen.forward(20)

turtle.done()