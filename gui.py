from tkinter import *
import main

def getDefComm():
    list1.delete(0, END)
    i = 1
    if isinstance(main.getDef(word_text.get()), str):
            list1.insert(END, main.getDef(word_text.get()))
    else:
       for defin in main.getDef(word_text.get()):
           list1.insert(END, str(i) + ". " + defin)
           i += 1
    e1.delete(0, "end")
    e2.delete(0, "end")

def addDefinComm():
    list1.delete(0, END)
    list1.insert(END, main.addDefin(word_text.get(), def_text.get()))
    e1.delete(0, "end")
    e2.delete(0, END)

def addPositionComm():
     list1.delete(0, END)
     list1.insert(END, main.addPosition(word_text.get(), def_text.get()))
     e1.delete(0, "end")
     e2.delete(0, "end")

def delPositionComm():
    list1.delete(0, END)
    list1.insert(END, main.delPosition(word_text.get()))
    main.delPosition(word_text.get())
    e1.delete(0, "end")
    e2.delete(0, "end")

def saveDicComm():
    list1.delete(0, END)
    list1.insert(END, main.saveDic())

window = Tk()
window.title("Dictionary")

l1 = Label(window, text = "Word")
l1.grid(row = 0, column = 0, sticky = "W")

l2 = Label(window, text = "Definition")
l2.grid(row = 1, column = 0, sticky = "W")

word_text = StringVar()
e1 = Entry(window, textvariable = word_text, width = 15)
e1.grid(row = 0, column = 1, sticky = "W")

def_text = StringVar()
e2 = Entry(window, textvariable = def_text, width = 30)
e2.grid(row = 1, column = 1, sticky = "W")

list1 = Listbox(window, height = 10, width = 80)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "Look up the word", width = 15, command = getDefComm)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Add the word", width = 15, command = addPositionComm)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add a definition", width = 15, command = addDefinComm)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Delete the word", width = 15, command = delPositionComm)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Save your dictionary", width = 15, command = saveDicComm)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Exit", width = 15, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()