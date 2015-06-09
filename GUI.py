from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import Core
import time

class Window_blank:

    def Change(self, haystack, needle):
        PrimSearch = Core.Primitive(haystack, needle)
        self.lbl8.configure(text = PrimSearch.get())
        BMSearch = Core.BoyerMoore(haystack, needle)
        self.lbl9.configure(text = BMSearch.get())
        BMHSearch = Core.BoyerMooreHorspool(haystack, needle)
        self.lbl10.configure(text = BMHSearch.get())
        RKSearch = Core.RabinKarp(haystack, needle, 1, 1)
        self.lbl11.configure(text = RKSearch.get())
        KMPSearch = Core.KnuthMorrisPratt(haystack, needle)
        self.lbl12.configure(text = KMPSearch.get())
        
    def __init__(self):

        main_menu = Menu(root)
        root.config(menu=main_menu)
        first_menu = Menu(main_menu)
        main_menu.add_cascade(label="File", menu=first_menu)
        first_menu.add_command(label="Open...", command=self.open_file)
        first_menu.add_command(label="Save As...", command=self.save_file)
        first_menu.add_command(label="About", command=self.about)
        first_menu.add_command(label="Exit", command=self.close_win)

        self.lbl1 = Label(root, text = "Enter the text:")
        self.lbl1.pack()
        self.lbl1.place(x = 34, y = 15)
        self.lbl2 = Label(root, text = "Enter the pattern:")
        self.lbl2.pack()
        self.lbl2.place(x = 15, y = 50)

        self.lbl3 = Label(root, text = "Primitive:")
        self.lbl3.pack()
        self.lbl3.place(x = 130, y = 150)
        self.lbl4 = Label(root, text = "Boyer-Moore Search:")
        self.lbl4.pack()
        self.lbl4.place(x = 69, y = 170)
        self.lbl5 = Label(root, text = "Boyer-Moore-Horspool Search:")
        self.lbl5.pack()
        self.lbl5.place(x = 15, y = 190)
        self.lbl6 = Label(root, text = "Rapin-Karp Search:")
        self.lbl6.pack()
        self.lbl6.place(x = 80, y = 210)
        self.lbl7 = Label(root, text = "Knuth-Morris-Pratt Search:")
        self.lbl7.pack()
        self.lbl7.place(x = 38, y = 230)

        self.lbl8 = Label(root, text = "")
        self.lbl8.pack()
        self.lbl8.place(x = 190, y = 150)
        self.lbl9 = Label(root, text = "pos: 0, time: 0.000009")
        self.lbl9.pack()
        self.lbl9.place(x = 190, y = 170)
        self.lbl10 = Label(root, text = "pos: 0, time: 0.000009")
        self.lbl10.pack()
        self.lbl10.place(x = 190, y = 190)
        self.lbl11 = Label(root, text = "pos: 0, time: 0.000009")
        self.lbl11.pack()
        self.lbl11.place(x = 190, y = 210)
        self.lbl12 = Label(root, text = "pos: 0, time: 0.000009")
        self.lbl12.pack()
        self.lbl12.place(x = 190, y = 230)
        
        v = StringVar()
        w = StringVar()
        self.ent1 = Entry(root, textvariable = v, width=40)
        self.ent1.pack()
        self.ent1.place(x = 120, y = 15)
        self.ent2 = Entry(root, textvariable = w, width=40)
        self.ent2.pack()
        self.ent2.place(x = 120, y = 50)
        
        self.btn = Button(root, text = "Search", command = lambda: self.Change(v.get(),w.get()))
        self.btn.pack()
        self.btn.place(x = 170, y = 100)
        
    def open_file(self):
        op = askopenfilename()
        try:
            self.ent1.delete(1.0, END)
            for i in fileinput.input(op):
                self.ent1.insert(END, i)
        except:
            pass
 
    def save_file(self):
        save_as = asksaveasfilename()
        try:
            letter = self.ent2.get(END, 1.0)
            f = open(save_as, "w")
            f.write(letter)
            f.close()
        except:
            pass
 
    def close_win(self):
        if askyesno("Save on close", "Do you want to save before closing?"):
            self.save_file()
            root.destroy()
        else:
            root.destroy()
 
    def about(self):
        showinfo("Editor Authors", "Substring Searcher (c)2015")
 
root = Tk()
root.title("Substring Searcher")
root.minsize(385, 400)
root.maxsize(385, 400)

obj_menu = Window_blank()
# Core.Whole(v.get(),w.get()
root.mainloop()
