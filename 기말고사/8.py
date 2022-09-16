from tkinter import *

def click(key):
    if key == '=':
        result = eval(entry.get())
        s = str(result)
        entry.insert(END, '=' + s)
    elif key == 'C':
        entry.delete(0, END)
    elif key == 'DEL':
        insert = entry.index("insert")
        entry.delete(insert - 1)
    else:
        entry.insert(END, key)

tk = Tk()
tk.title('간단한 계산기')
entry = Entry(tk, width=27, bg='white')
entry.grid(row=0, column=0, columnspan=5)

buttonList = ['C','(',')','+','//',
              '1','2','3','-','%',
              '4','5','6','*','**',
              '7','8','9','/',' ',
              '0','.','DEL','=']

rowIndex = 1
colIndex = 0

for buttonText in buttonList:
    Button(tk, text=buttonText, width=5, command=lambda t = buttonText : click(t)).grid(row=rowIndex, column=colIndex)

    colIndex += 1
    if colIndex > 4:
        rowIndex += 1
        colIndex = 0

tk.mainloop()