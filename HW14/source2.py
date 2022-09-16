import turtle, random

line_turtle = turtle.Turtle()
line_turtle.penup()
line_turtle.setposition(200,50)
line_turtle.pendown()
line_turtle.setposition(200,-50)

line_turtle.hideturtle()

Tom = turtle.Turtle()
Tom.shape('turtle')
Tom.penup()
Tom.setposition(-100,20)

Sam = turtle.Turtle()
Sam.shape('turtle')
Sam.penup()
Sam.setposition(-100,-20)

Tom_sum = 0
Sam_sum = 0

while Tom_sum < 300 and Sam_sum < 300:
    Tom_distance = random.randint(1,10)
    Tom.forward(Tom_distance)
    Tom_sum += Tom_distance

    Sam_distance = random.randint(1,10)
    Sam.forward(Sam_distance)
    Sam_sum += Sam_distance

if Tom_sum > Sam_sum:
    Tom.color('blue')
    Sam.color('red')
else:
    Tom.color('red')
    Sam.color('blue')

turtle.mainloop()