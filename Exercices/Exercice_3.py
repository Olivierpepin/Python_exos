# Exercices_03 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_03.md

# Loops exercices

## Exercice 1 - Level 1

# 1 Iterate 0 to 10 using for loop, do the same using while loop.

i = 0
while i <= 10:
    print(i)
    i += 1

# With "for" loop

for i in range(0,11):
    print(i)


# 2 Iterate 10 to 0 using for loop, do the same using while loop.

i=10
while i >= 0:
    print(i)
    i -= 1

# With "for" loop

for i in range(10,-1,-1): # Begin / End (-1) / Step
    print(i)


# 3 Write a loop that makes seven calls to print(). See md for the output.

## For further informations about Nested loops : 
## https://pynative.com/python-nested-loops/#:~:text=Loop%20in%20Python%3F-,What%20is%20a%20Nested%20Loop%20in%20Python%3F,while%20loop%20and%20vice%20versa.

for i in range (1,9):
    print(i*'# ')

# With Outer and Inner loops

n = int(input("Nombre de lignes : "))  
for i in range(0, n):   
    for j in range(0, i + 1):  
        print('# ', end = '')
    print()



# 4 Use nested loops to create the following. See md for the output.

n = int(input("Nombre de lignes : "))
for i in range(n):
    for i in range(n):
        print('# ', end = '')
    print()


# 5 Print the following pattern. See md for the output.

for i in range(0,11):
    print(i, ' x ', i, ' = ', i*i)


# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.

list = ['Python','Numpy','Pandas','Django','Flask']

for i in list:
    print(i)

# While loop. The lenght is needed. 

list = ['Python','Numpy','Pandas','Django','Flask']

lenght = len(list)
i = 0

while i < lenght:
    print(list[i])
    i += 1


# 7 Use for loop to iterate from 0 to 100 and print only even numbers

# Utilisation d'un pas

for i in range(0,101,2):
    print(i)


# La condition est l'affichage des chiffres paires. Il est donc pas necessaire d'interroger les chiffres impaires.
# Nous pouvons nous limiter à un "if". L'absence de check sur les impairs pourrait occasionner des problèmes
# des cas complexes.

for i in range(0,101):
    if (i%2) == 0: print(i)


# 8 Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(0,101):
    if (i%2) != 0: # Different de 0
        print(i)

# one line

for i in range(0,101):
    if (i%2) != 0: print(i)


## Exercice 2 - Level 2

# 1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for i in range(0,101):
    sum += i
print(sum)


# 1.1 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

somme_even = 0
somme_odd = 0
for i in range(0,101):
    if (i%2) == 0:
        somme_even += i 
    else:
        somme_odd += i
print('La somme des nombres paires est', somme_even)
print('La somme des nombres impaires est', somme_odd)


# Exercice 3 - Level 3

# 1 Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

# import d'un fichier

import countries

from countries import countries_list # "*" pour import all comme SQL

newlist = []

for country in countries_list:
    if 'land' in country:
        newlist.append(country)
print(newlist)


''' Voir pour une utilisation avec compile()

import countries

from countries import *

r = countries.compile(".*land.*")
newlist = list(filter(r.match, countries))
print(newlist)'''


# 2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

# On va récuperer indivuduellement chaque element de l'array en partant du dernier "[::-1]" et chaque
# element va être ajouté individuellement en incrémentant l'index.

fruits = ['banana', 'orange', 'mango', 'lemon']

newfruit = []
for i in fruits[::-1]:
    newfruit.append(i) 
print(newfruit)

# L'array va être lu dans le sens de l'index mais chaque entrées va être poussées de +1 par une nouvelle entrée
# car insert() attribura à chaque nouvelle entrée l'index 0

fruits=['banana', 'orange', 'mango', 'lemon']

rev_fruits=[]
for fruit in fruits:
    rev_fruits.insert(0,fruit)
print (rev_fruits)

# Avec la fonction reverse

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.reverse()
print(fruits)


# Exercice 3 Go to the data folder and use the countries_data.py file

# i What are the total number of languages in the data

# Le but est de récupérer l'ensemble des langages dans contriesdata et de les ajouter dans
# une nouvelle liste. Une somme des index est ensuite imprimé afin de supprimer les doublons.

import countriesdata

from countriesdata import *

liste_langues = []
for country in countriesdata:
    liste_langues.extend(country["languages"])

print(len(set(liste_langues)))

# ii Find the ten most spoken languages from the data

import countriesdata

from countriesdata import *

LangList={}
# on parcours les pays
for cntData in countriesdata:
	DictLanguages = cntData['languages']
	# on parcours les langages du pays
	for Lang in DictLanguages:
		# on parcours les langues présentes
		bPresente=False
		for LangTest in LangList:
			if LangTest == Lang:
				bPresente=True
				LangList[LangTest] = LangList[LangTest]+1
		if bPresente == False: 
			LangList[Lang] = 1
#LangList.sort()
sorted_Lang = dict( sorted(LangList.items(),
			key=lambda item: item[1],
			reverse=True))

max=10
for Lang in sorted_Lang:
	print (Lang)
	max=max-1
	if max == 0:
		break

# iii Find the 10 most populated countries in the world

# A travailler. Manque sort par pays et population

'''import countriesdata

from countriesdata import *
dict = {}
for country in countriesdata:
    dict.append(country["name"],country["population"])

print(dict)'''
