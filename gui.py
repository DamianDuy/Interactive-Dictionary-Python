from tkinter import *
from main import Dictionary

dictionary = Dictionary()

class Widgets:
   def __init__(self, window):
       self.window = window
       window.title("Dictionary")

       l1 = Label(window, text = "Word")
       l1.grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 1)

       l2 = Label(window, text = "Definition")
       l2.grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 1)

       self.word_text = StringVar()
       self.e1 = Entry(window, textvariable = self.word_text, width = 30)
       self.e1.grid(row = 0, column = 1, sticky = "W")

       self.def_text = StringVar()
       self.e2 = Entry(window, textvariable = self.def_text, width = 30)
       self.e2.grid(row = 1, column = 1, sticky = "W")

       self.list1 = Listbox(window, height = 10, width = 80)
       self.list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2, padx = 5, pady = 5)

       sb1 = Scrollbar(window)
       sb1.grid(row = 2, column = 2, rowspan = 6)

       self.list1.configure(yscrollcommand = sb1.set)
       sb1.configure(command = self.list1.yview)

       b1 = Button(window, text = "Look up the word", width = 15, command = self.getDefComm)
       b1.grid(row = 2, column = 3, padx = 5, pady = 5)

       b2 = Button(window, text = "Add the word", width = 15, command = self.addPositionComm)
       b2.grid(row = 3, column = 3, padx = 5, pady = 5)

       b3 = Button(window, text = "Add a definition", width = 15, command = self.addDefinComm)
       b3.grid(row = 4, column = 3, padx = 5, pady = 5)

       b4 = Button(window, text = "Delete the word", width = 15, command = self.delPositionComm)
       b4.grid(row = 5, column = 3, padx = 5, pady = 5)

       b5 = Button(window, text = "Save your dictionary", width = 15, command = self.saveDicComm)
       b5.grid(row = 6, column = 3, padx = 5, pady = 5)

       b6 = Button(window, text = "Exit", width = 15, command = window.destroy)
       b6.grid(row = 7, column = 3, padx = 5, pady = 5)

   def getDefComm(self):
       self.list1.delete(0, END)
       i = 1
       if isinstance(dictionary.getDef(self.word_text.get()), str):
           self.list1.insert(END, dictionary.getDef(self.word_text.get()))
       else:
          for defin in dictionary.getDef(self.word_text.get()):
              self.list1.insert(END, str(i) + ". " + defin)
              i += 1
       self.e1.delete(0, "end")
       self.e2.delete(0, "end")

   def addDefinComm(self):
       self.list1.delete(0, END)
       self.list1.insert(END, dictionary.addDefin(self.word_text.get(), self.def_text.get()))
       self.e1.delete(0, "end")
       self.e2.delete(0, END)

   def addPositionComm(self):
        self.list1.delete(0, END)
        self.list1.insert(END, dictionary.addPosition(self.word_text.get(), self.def_text.get()))
        self.e1.delete(0, "end")
        self.e2.delete(0, "end")

   def delPositionComm(self):
       self.list1.delete(0, END)
       self.list1.insert(END, dictionary.delPosition(self.word_text.get()))
       dictionary.delPosition(self.word_text.get())
       self.e1.delete(0, "end")
       self.e2.delete(0, "end")

   def saveDicComm(self):
       self.list1.delete(0, END)
       self.list1.insert(END, dictionary.saveDict())

window = Tk()
Widgets(window)
window.mainloop()