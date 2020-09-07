from tkinter import *
import main
window = Tk()

def getDefComm():
    for defin in main.getDef(key):
        list1.delete(0, End)
        list1.insert(END, defin)


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

list1 = Listbox(window, height = 10, width = 40)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "Look up the word", width = 15)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Add the word", width = 15)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add a definition", width = 15)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Delete the word", width = 15)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Save your dictionary", width = 15)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Exit", width = 15)
b6.grid(row = 7, column = 3)

window.mainloop()