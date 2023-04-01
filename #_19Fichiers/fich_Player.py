#coding:utf-8


"""
dump(variable) sert à créer une copie avec le module pickle (copie de l'objet)
Pickler(variable) sert à spécifier l'endroit d'enregistrement du fichier
Au format (.txt) le résultat ne seras pas le même que le résultat avoir glissé déposé
sur Sublime Text
"""
class Player:
	"""docstring for Player"""
	def __init__(self, name, level):

		self.name = name
		self.level = level

	def whoami(self):
		print(f"name:	{self.name}	level:	{self.level}")

#if __name__ == "__main__":
import pickle
p1 = Player("J_Son_file", "Level upgrade")
#(print dans un print ne sert à rien!!!)
p1.whoami()

with open("player.data", "wb") as fic:
	record = pickle.Pickler(fic)
	record.dump(p1)