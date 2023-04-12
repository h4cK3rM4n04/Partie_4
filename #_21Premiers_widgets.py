#coding:utf-8
import tkinter
def win_custom():

	win.title("#_21Premiers_Widgets")
	win.config(background = "darkgrey")
	screen_x = win.winfo_screenwidth() #récupère la résolution de l'écran
	#print(screen_x)
	screen_y = win.winfo_screenheight()
	#print(screen_y)
	window_mainapp_x = 900
	window_mainapp_y = 700
	posX = (screen_x // 2 - window_mainapp_x // 2)
	posY = (screen_y // 2 - window_mainapp_y // 2)
	geom = f"{window_mainapp_x}x{window_mainapp_y}+{posX}+{posY}"
	win.geometry(geom)
	win.minsize(300,300)
	win.maxsize(800,700)
	label_1 = tkinter.Label(win, text ='Bonjour je suis un TEXTE')
	label_1.pack()
	print(label_1.cget("text"))
	label_1.config(text = "Bonjour je suis le nouveau texte", background = "darkgrey")
	message_1 = tkinter.Message(win, text = "Message__ERROR__", background = "darkred")
	message_1.pack()
	entry_1 = tkinter.Entry(win, width = 45, exportselection = 0)
	entry_1.pack()
	button_quit = tkinter.Button(win, text = "Alt F4", width = 24, command = win.quit)
	button_quit.pack()
	

win = tkinter.Tk()

win_custom()

win.mainloop()