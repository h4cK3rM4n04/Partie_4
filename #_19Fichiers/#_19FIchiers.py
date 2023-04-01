#coding:utf-8

"""
Modes d'ouvertures:		r(lecture seule)
						w(écriture avec remplacement)
						a(écriture avec ajout en fin de fichier)
						x(lecture et écriture)
						r+(lecture/écriture dans un même fichier)

Modes de lectures:		file.read() ; file.readline(); file.readlines()
Pas besoin de fermer le fichier avec with open(file,"sdqs") as variable:

Essayez de ne pas mettre l'extension du fichier pour voir le magnifique résultat!!!

"""

file = open("file_D/file_0.txt", "r")

nombre = 155497984566135456
content = file.read()
content = int(content)
print("Après avoir ajouté nombre à content on obtient donc:	", nombre + content, "\n")

file.close()

with open("file_D/file_1.txt", "r") as x:
	#On peut le mettre dans une variable ce n'est pas un problème.......
	print(x.read())

with open("file_D/file_2.txt", "w") as  file:
	nombre = 155497984566135456
	file.write(str(nombre) + "\n")
	file.write("Bonjour je suis h4cK3rM4n04")
print(True or False)