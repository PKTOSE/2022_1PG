from tkinter import *

def add():
    result = '출력: ' + str(float(entryA.get()) + float(entryB.get()))
    print(result)
    labRst.configure(text = result)

def sub():
    result = '출력: ' + str(float(entryA.get()) - float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def mul():
    result = '출력: ' + str(float(entryA.get()) * float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def div():
    result = '출력: ' + str(float(entryA.get()) / float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def user():
    result = '출력: ' + str(int(float(entryA.get())) ** int(float(entryB.get())))
    print(result)
    labRst.configure(text=result)

tk = Tk()
tk.title('Calcul')
tk.geometry('500x50')

Label(tk, text = '입력 A: ', width=5).pack(side=LEFT)

entryA = Entry(tk,width=5)
entryA.insert(0,'0')
entryA.pack(side=LEFT)

Label(tk, text='입력 B: ', width=5).pack(side=LEFT)

entryB = Entry(tk, width=5)
entryB.insert(0, '0')
entryB.pack(side=LEFT)

Label(tk, text='연산: ', width=5).pack(side=LEFT)

btnAdd = Button(tk, text='+', width=3, command=add)
btnAdd.pack(side=LEFT)
btnSub = Button(tk, text='-', width=3, command=sub)
btnSub.pack(side=LEFT)
btnMul = Button(tk, text='x', width=3, command=mul)
btnMul.pack(side=LEFT)
btnDiv = Button(tk, text='/', width=3, command=div)
btnDiv.pack(side=LEFT)
btnUser = Button(tk, text='@', width=3, command=user)
btnUser.pack(side=LEFT)

labRst = Label(tk, text='출력: 0.0', width=20, anchor='w')
labRst.pack(side=LEFT)

tk.mainloop()