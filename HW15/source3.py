from tkinter import *

xCur , yCur = None, None
colourCur = 'black'

def drawCanvas():
    canvas.delete('all')
    widthCur = entry.get()
    canvas.create_text(100, 100, fill='green', font='Arial 30 italic bold', text="TEXT")
    canvas.create_line(50, 150, 50, 200, capstyle=ROUND, width=widthCur, fill='red')
    canvas.create_rectangle(100, 150, 150, 200, width=widthCur, outline='red')
    canvas.create_polygon(200, 150, 250, 150, 250, 200, fill='blue')
    var.set(entry.get())

def resetCanvas():
    canvas.delete('all')

def draw(event):
    global xCur, yCur
    if xCur and yCur:
        widthCur = event.get()
        var.set(entry.get())
        canvas.create_line(xCur, yCur, event.x, event.y, capstyle=ROUND, width=widthCur, fill=colourCur)
    xCur = event.x
    yCur = event.y

def reset(event):
    global xCur, yCur
    xCur, yCur = None, None

def toggle(event):
    global colourCur
    if colourCur == 'white':
        colourCur = 'black'
    else:
        colourCur = 'white'

tk = Tk()
tk.title('Lab')
label = Label(tk, text='선굵기: ')
label.grid(row=0, column=0)

entry = Entry(tk)
entry.grid(row=0, column=1)
entry.insert(0, '5')

image = PhotoImage(file='apple.png')
img = Label(tk, image=image)
img.grid(row=1, columnspan=2, sticky=W+E)

btnDraw = Button(tk, text='그리기', command=drawCanvas)
btnDraw.grid(row=2, columnspan=2, sticky=W+E)
rstErase = Button(tk, text='지우기', command=resetCanvas)
rstErase.grid(row=3, columnspan=2, sticky=W+E)

canvas = Canvas(tk, bg='white', bd='2', width=300, height=300)
canvas.grid(row=4, columnspan=2)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', reset)
canvas.bind('<Button-3>', toggle)

var = DoubleVar()
slider = Scale(tk, variable=var, orient=HORIZONTAL)
slider.grid(row=5, columnspan=2, sticky=W+E)

tk.mainloop()