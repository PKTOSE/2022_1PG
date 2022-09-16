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

def drawStar(x,y,size):
    t1.setheading(0)
    moveTo(x,y)
    for i in range(5):
        t1.forward(size)
        t1.right(180-36)


width = turtle.window_width()
height = turtle.window_height()
dividwindow = width/3
left = -(width/3)
right = width/3
left1 = left
right1 = left + dividwindow
left2 = right1
right2 = right
left3 = right2
right3 = right1

shapewidth = dividwindow * 0.8

x1 = left1
y1 = height * 0.1

x2 = left2 + dividwindow * 0.5
y2 = height * 0.1

x3 = x2 + dividwindow * 0.5
y3 = height * 0.1

drawRectangle2(x1, y1, shapewidth, shapewidth)
t1.setheading(0)
drawTriangle(x2,y2,shapewidth)
drawStar(x3,y3,shapewidth)

turtle.mainloop()