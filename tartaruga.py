import turtle

star = turtle.Turtle()
star.shape('turtle')

for i in range(10):
    star.forward(i)
    star.forward(100)
    star.right(144)

turtle.done()