#coding:utf-8
import tkinter
#from tkinter import Tk
"""
tout dans une fenetre est un widget
variable.resizable(width=True ou False, height=True ou False) Donne l'autorisation
de modification ou non de la résolution de la fenetre...!

mainapp.positionfrom("user") } Try
mainapp.sizefrom("user")	 } Try

Mettre la fenetre au milieu de l'écran
positionX = (largeur_de_mon_écran_ // 2 - largeur_fenetre // 2)
positionY = (hauteur_de_mon_écran // 2 - hauteur_fenetre // 2)
"""

mainapp = tkinter.Tk()

screen_x = mainapp.winfo_screenwidth() #récupère la résolution de l'écran
#print(screen_x)
screen_y = mainapp.winfo_screenheight()
#print(screen_y)
window_mainapp_x = 340
window_mainapp_y = 250
posX = (screen_x // 2 - window_mainapp_x // 2)
posY = (screen_y // 2 - window_mainapp_y // 2)
geom = f"{window_mainapp_x}x{window_mainapp_y}+{posX}+{posY}"

mainapp.title("h4cK3rM4n04")
mainapp.geometry(geom)
#mainapp.minsize(300, 200)
mainapp.maxsize(350, 250)
mainapp.resizable(width = False, height = False)
mainapp.config(background = "black")
mainapp.positionfrom("user")

mainapp.mainloop()