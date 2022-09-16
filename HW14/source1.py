import turtle

win = turtle.Screen()
t1 = turtle.Turtle()

def moveTo(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()

def drawRectangle2(x,y,w,h):
    moveTo(x,y)
    t1.goto(x+w,y)
    t1.goto(x+w,y-h)
    t1.goto(x,y-h)
    t1.goto(x,y)

def drawTriangle(x,y,size):
    t1.setheading(0)
    moveTo(x,y)
    t1.right(60)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)

width = turtle.window_width()
height = turtle.window_height()
dividwindow = width/2
left = -(width/2)
right = width/2
left1 = left
right1 = left + dividwindow
left2 = right1
right2 = right

shapewidth = dividwindow * 0.8

x1 = left1 + dividwindow * 0.1
y1 = height * 0.1

x2 = left2 + dividwindow * 0.5
y2 = height * 0.1

drawRectangle2(x1, y1, shapewidth, shapewidth)
t1.setheading(0)
drawTriangle(x2,y2,shapewidth)

turtle.mainloop()