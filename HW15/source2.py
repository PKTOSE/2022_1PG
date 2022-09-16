from tkinter import *

def click(key):
    if key=='=':
        result = eval(entry.get())
        s = str(result)
        entry.insert(END, '=' + s)
    elif key == '@':
        entry.delete(0, END)
    else:
        entry.insert(END, key)

tk = Tk()

entry = Entry(tk, width=25, bg='white')
entry.grid(row=0, column=0, columnspan=4)

buttonList = ['1','2','3','+','4','5','6','-','7','8','9','*','0','.','=','@']

rowIndex = 1
colIndex = 0

for buttonText in buttonList:
    Button(tk, text=buttonText, width=5, command=lambda t = buttonText : click(t)).grid(row=rowIndex, column=colIndex)

    colIndex += 1
    if colIndex > 3:
        rowIndex += 1
        colIndex = 0

tk.mainloop()