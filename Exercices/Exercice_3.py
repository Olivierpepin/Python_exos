# Exercices_03 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_03.md

# Loops exercices

## Exercice 1 - Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

# With for loop

for i in range(0,11):
    print(i)



# Exercice 1.2
for i in range(10,-1,-1):
    print(i)

i=10
while i >= 0:
    print(i)
    i -= 1

# Exercice 1.3

n = int(input("Nombre de lignes : "))  
for i in range(0, n):   
    for j in range(0, i + 1):  
        print('# ', end = '')           
    print()  

for i in range (1,8):
    print(i*'#')

# Exercice 1.4

cote = int(input("Nombre de lignes : "))
for i in range(cote):
    for i in range(cote):
        print('# ', end = '')
    print()

# Exercice 1.5

for i in range(0,11):
    print(i, ' x ', i, ' = ', i*i)

# Exercice 1.6

list = ['Python','Numpy','Pandas','Django','Flask']
for i in list:
    print(i)

# Exercice 1.7

for i in range(0,101,2):
    print(i)

for i in range(0,101):
    if (i%2) == 0:
        print(i)
    else:
        continue

# Exercice 1.8

for i in range(0,101):
    if (i%2) != 0:
        print(i)
    else:
        continue

# Exercice 2.1

somme = 0
for i in range(0,101):
    somme += i
print('La somme est egale a ', somme)

# Exercice 2.2

somme_even = 0
somme_odd = 0
for i in range(0,101):
    if (i%2) == 0:
        somme_even += i 
    else:
        somme_odd += i
print('La somme des nombres paires est', somme_even)
print('La somme des nombres impaires est', somme_odd)

# Exercice 3.1

countries=['Afghanistan','Albania','Algeria','Andorra','Angola','AntiguaandBarbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','BosniaandHerzegovina','Botswana','Brazil','Brunei','Bulgaria','BurkinaFaso','Burundi','Cambodia','Cameroon','Canada','CapeVerde','CentralAfricanRepublic','Chad','Chile','China','Colombi','Comoros','Congo(Brazzaville)','Congo','CostaRica',"Coted'Ivoire",'Croatia','Cuba','Cyprus','CzechRepublic','Denmark','Djibouti','Dominica','DominicanRepublic','EastTimor(TimorTimur)','Ecuador','Egypt','ElSalvador','EquatorialGuinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia,The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea,North','Korea,South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','MarshallIslands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','NewZealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','PapuaNewGuinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','SaintKittsandNevis','SaintLucia','SaintVincent','Samoa','SanMarino','SaoTomeandPrincipe','SaudiArabia','Senegal','SerbiaandMontenegro','Seychelles','SierraLeone','Singapore','Slovakia','Slovenia','SolomonIslands','Somalia','SouthAfrica','Spain','SriLanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','TrinidadandTobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','UnitedArabEmirates','UnitedKingdom','UnitedStates','Uruguay','Uzbekistan','Vanuatu','VaticanCity','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',]

newlist = []
for country in countries:
    if 'land' in country:
        newlist.append(country)
print(newlist)

import re
r = re.compile(".*land.*")
newlist = list(filter(r.match, countries))
print(newlist)

# Exercice 3.2

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

newfruit = []
for i in fruits[::-1]:
    newfruit.append(i)
print(newfruit)

# Exercice 3.3
# i

from countries_data import *
liste_langues = []
for country in countries_data:
    liste_langues.extend(country["languages"])

print(len(set(liste_langues)))

# ii


# iii

from countries_data import *
dict = {}
for country in countries_data:
    dict.append(country["name"],country["population"])
