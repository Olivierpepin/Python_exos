# Open a file in the same folder (path not required)

file = open("test2.txt","r") # Ouverture d'un fichier en lecture
# file = open("text.txt", "w") # Ouverture en ecriture
# Differentes methodes de recuperation de file

# x = file.read() # recupere l'integralite des strings
# x = file.readline() # recupere une ligne en strings
x = file.readlines() # recupere toutes les lignes dans un array

# print(type(x))

# print(x)

for line in x:                      # Pour chaque ligne dans x (test2.txt)
    line = line.replace("\n", "")   # Remplace le retour à la ligne par du vide
    liste = line.split(',')         # Decoupe le texte en string sur le caractère ","
    liste.pop(1)                    # Enleve l'element à l'index 1 de la ligne
    list_int = []                   # Creation d'une liste vide
    for x in liste:                 # Pour chaque element dans la ligne
        list_int.append(int(x))     # On rajoute ses elements à une nouvelle liste en les transformant en integer
    print(list_int[0:2])            # Impression de la liste avec conditions

# Second exemple sur fichier text.txt

file = open("text.txt", "r")

x = file.read() # Lecture de l'integralite du fichier en string

# print(x)

for line in x.split("\n"):
    liste = line.split(', ')
    liste[1] = int(liste[1])
    print(liste[1])

lines = file.readlines()

for line in lines:
    line = line.replace("\n", "")
    print(line.split(","))

# Avec len

file = open("text.txt", "r")
# file = open("text.txt", "w")


lines = file.readlines()

for line in lines:
    line = line.replace("\n", "")
    print(len(line.split(",")))