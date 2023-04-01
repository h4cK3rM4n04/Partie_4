#coding:utf-8

"""
Création d'un dictionnaire
nom_dico = {clée: valeur, clée: valeur...etc}
supression: 	name.pop(clée)
				del name.clée

"""
dico = [{"nom": "h4cK3rM4__4", "prénom": "M4__4"},
		{"nom": "Ch__é", "prénom": "Ch__é"}]
print(dico[0]["nom"], dico[1]["nom"])

"""
Copie de dictionnaire:		dico1{"bonjour": 10}
							dico2 = dico1.copy()

							""

#Création d'un résultat d'un None type!!! **pa peut prendre plusieurs valeurs
def dicoé(**pa):
	print(pa)
print(type(dicoé(p = "bonjour", v ="au revoir", c = (121,))))

mydict = {"device": "laptop" , "constructeur": "acer" , "ram": "8G" , 
"processeur": "Intel core i5", "stockage": "500 G"}

mydict["stockage"] = "750 G"

x = [x for x in mydict.keys()]
y = [x for x in mydict.values()]
z = []

for x, y in mydict.items():
	z += x, y
print(z)

"""inverser les clées:valeurs  processeur et stockage"""