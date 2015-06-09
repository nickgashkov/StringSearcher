# -*- coding: utf-8 -*-
"""GUI by tkinter for string searching algorithms provided algorithms.py

implemented algorithms:
Naive string search algorithm
Boyer-Moore string search algorithm
Boyer-Moore-Horspool string search algorithm
Rabin-Karp string search algorithm
Knuth-Morris-Pratt string search algorithm

"""

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

import fileinput
import time

import algorithms

class UserInterface:

    def __init__(self):
        """Main function containing all widgets related to app

        keyword arguments:
        self -- object to place on frame, configure parametrs e.t.c

        """
        # Variables
        text = StringVar()
        pattern = StringVar()

        # Menu
        mainMenu = Menu(root)
        root.config(menu = mainMenu)
        firstMenu = Menu(mainMenu)
        mainMenu.add_cascade(label = "File", menu = firstMenu)
        firstMenu.add_command(label = "About", command = self.about)
        firstMenu.add_command(label = "Exit", command = self.close_app)

        # Labels
        self.textEntryLabel = Label(root, text = "Enter the text:", background='#f0f8ff')
        self.textEntryLabel["fg"] = "#00527a"
        self.textEntryLabel.grid(row = 3, column = 1, columnspan = 2, sticky = E)

        self.patternEntryLabel = Label(root, text = "Enter the pattern:", background='#f0f8ff')
        self.patternEntryLabel["fg"] = "#00527a"
        self.patternEntryLabel.grid(row = 4, column = 1, columnspan = 2, sticky = E)

        self.naiveLabel = Label(root, text = "Naive:", background='#f0f8ff')
        self.naiveLabel["fg"] = "#00527a"
        self.naiveLabel.grid(row = 6, column = 1, columnspan = 2, sticky = E)
        self.bmLabel = Label(root, text = "Boyer-Moore:", background='#f0f8ff')
        self.bmLabel["fg"] = "#00527a"
        self.bmLabel.grid(row = 7, column = 1, columnspan = 2, sticky = E)
        self.bmhLabel = Label(root, text = "Boyer-Moore-Horspool:", background='#f0f8ff')
        self.bmhLabel["fg"] = "#00527a"
        self.bmhLabel.grid(row = 8, column = 1, columnspan = 2, sticky = E)
        self.rkLabel = Label(root, text = "Rabin-Karp:", background='#f0f8ff')
        self.rkLabel["fg"] = "#00527a"
        self.rkLabel.grid(row = 9, column = 1, columnspan = 2, sticky = E)
        self.kmpLabel = Label(root, text = "Knuth-Morris-Pratt:", background='#f0f8ff')
        self.kmpLabel["fg"] = "#00527a"
        self.kmpLabel.grid(row = 10, column = 1, columnspan = 2, sticky = E)

        self.naiveResultLabel = Label(root, background='#f0f8ff')
        self.naiveResultLabel["fg"] = "#004161"
        self.naiveResultLabel.grid(row = 6, column = 3, columnspan = 2, sticky = W)
        self.bmResultLabel = Label(root, background='#f0f8ff')
        self.bmResultLabel["fg"] = "#004161"
        self.bmResultLabel.grid(row = 7, column = 3, columnspan = 2, sticky = W)
        self.bmhResultLabel = Label(root, background='#f0f8ff')
        self.bmhResultLabel["fg"] = "#004161"
        self.bmhResultLabel.grid(row = 8, column = 3, columnspan = 2, sticky = W)
        self.rkResultLabel = Label(root, background='#f0f8ff')
        self.rkResultLabel["fg"] = "#004161"
        self.rkResultLabel.grid(row = 9, column = 3, columnspan = 2, sticky = W)
        self.kmpResultLabel = Label(root, background='#f0f8ff')
        self.kmpResultLabel["fg"] = "#004161"
        self.kmpResultLabel.grid(row = 10, column = 3, columnspan = 2, sticky = W)

        self.titleLabel = Label(root, text = "StringSearcher", background = '#f0f8ff')
        self.titleLabel["fg"] = "#00527a"
        self.titleLabel.config(font='bold')
        self.titleLabel.grid(row = 1, column = 1, columnspan = 4, padx = 5, pady = 5)

        self.indentTop = Label(root, text = "", background = '#f0f8ff')
        self.indentTop.grid(row = 0, column = 0, columnspan = 4, sticky = E, padx = 5, pady = 5)
        self.indentTitle = Label(root, text = "", background = '#f0f8ff')
        self.indentTitle.grid(row = 2, column = 0, columnspan = 4, sticky = E, padx = 5, pady = 5)
        self.indentLeft = Label(root, text = "", background = '#f0f8ff')
        self.indentLeft.grid(row = 0, column = 0, rowspan = 11, sticky = E, padx = 5, pady = 5)
        self.indentBottom = Label(root, text = "", background = '#f0f8ff')
        self.indentBottom.grid(row = 11, column = 0, columnspan = 4, sticky = E, padx = 5, pady = 5)
        self.indentRight = Label(root, text = "", background = '#f0f8ff')
        self.indentRight.grid(row = 0, column = 4, rowspan = 11, sticky = E, padx = 5, pady = 5)

        # Entries
        self.textEntry = Entry(root, textvariable = text)
        self.textEntry.grid(row = 3, column = 3, columnspan = 2)
        self.patternEntry = Entry(root, textvariable = pattern)
        self.patternEntry.grid(row = 4, column = 3, columnspan = 2)

        # Buttons
        self.searchButton = Button(root, text = "Search", background='#7fa8bc', width = 20, command = lambda: self.search(text.get(), pattern.get()))
        self.searchButton["fg"] = "#003955"
        self.searchButton.grid(row = 5, column = 2, columnspan = 2, padx = 5, pady = 5)

    def about(self):
        """Adds "About" to cascade

        keyword arguments:
        self -- object to place on frame, configure parametrs e.t.c

        """
        showinfo("Editor Authors", "StringSearcher ©2015")

    def close_app(self):
        """Adds "Exit" to cascade

        keyword arguments:
        self -- object to place on frame, configure parametrs e.t.c

        """
        if askyesno("Verify", "Are you sure?"):
            root.destroy()

    def search(self, haystack, needle):
        """Main function allowing communicate between app.py and algorithms.py

        keyword arguments:
        self -- object to place on frame, configure parametrs e.t.c

        """
        naive_search = algorithms.naive(haystack, needle)
        self.naiveResultLabel.configure(text = naive_search.get())
        bm_search = algorithms.boyer_moore(haystack, needle)
        self.bmResultLabel.configure(text = bm_search.get())
        bmh_search = algorithms.boyer_moore_horspool(haystack, needle)
        self.bmhResultLabel.configure(text = bmh_search.get())
        rk_search = algorithms.rabin_karp(haystack, needle, 257, 11)
        self.rkResultLabel.configure(text = rk_search.get())
        kmp_search = algorithms.knuth_morris_pratt(haystack, needle)
        self.kmpResultLabel.configure(text = kmp_search.get())

root = Tk()
root.title("StringSearcher")
root.configure(background = "#f0f8ff")
root.geometry('295x300') 
root.resizable(width = FALSE, height = FALSE)

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

app = UserInterface()
root.mainloop()
