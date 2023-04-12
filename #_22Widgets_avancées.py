#coding:utf-8
from tkinter import *
from tkinter import messagebox

"""
quelques méthodes de tkinter.messagebox
messagebox.showerror()
messagebox.showwarning()
messagebox.askquestion()
messagebox.info()
messagebox.askokcancel()

"""

win = Tk()
win.title("#_22Widgets_avancées")
win.minsize(500, 300)
win.maxsize(1100, 700)
win.geometry("900x750")
persentation = Label(win, text = "Présentation of Many widgets with tkinter (Python)", font = ("Old English Text MT", 30),
	fg = "red")
persentation.pack()
check_button = Checkbutton(win, text = "Check", offvalue = 1, onvalue = 2, height = 2, width = 5, background = "darkgrey")
check_button.pack()
radio_w_1 = Radiobutton(win, text = "radio 1", value = 1)
radio_w_2 = Radiobutton(win, text = "radio 2", value = 0)
radio_w_1.pack()
radio_w_2.pack()
scale_txt = Label(win, text = "Scale:	", fg = "darkblue", bg = "white", font = ("Old English Text MT", 15))
scale_txt.pack()
scale_w = Scale(win, from_ = 0, to = 10, tickinterval = 3, width = 25)
scale_w.pack(side = RIGHT) 
spin_w = Spinbox(win, from_ = 10, to = 100, width = 180)
spin_w.pack(side = BOTTOM)
list_box = Listbox(win, width = 50, height = 10)
list_box.insert(1, "Windows (Système d'explotation depuis longtemps)")
list_box.insert(2, "Linux (Système d'exploitation pour le hacking)")
list_box.insert(3, "Mac OS (Système d'exploitation pour Travailler)")
list_box.pack()

#tkinter message box============================================================================
def message():
	messagebox.showerror("Erreur", "Un erreur est survenu votre machine va exploser")

buton = Button(win, text = "QUIT", command = message, fg = "green", bg = 'black', width = 10, height = 5)
buton.pack()
win.mainloop()