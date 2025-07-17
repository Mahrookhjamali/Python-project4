import turtle
screen = turtle.Screen()
screen.bgcolor("green")  
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
for _ in range(4):
    pen.backward(100)  # Move forward
    pen.left(90)
screen.exitonclick()
