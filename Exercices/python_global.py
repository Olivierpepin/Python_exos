# Exercices_01
# Conditionals exercises

### Exercise 1.1

saisie = input('Entrer votre age : ') 
saisie = int(saisie)
if saisie >= 18:
    print('Tu es assez age pour apprendre a conduire.')
else:
    diff = 18 - saisie 
    print('Tu dois attendre ' + str(diff) + ' annee(s) pour apprendre a conduire.')

### Exercise 1.2

son_age = int(input('Entrer son age : '))
votre_age = int(input('Entrer votre age : '))
diff = votre_age - son_age
if son_age < votre_age:
    print('Vous etes' + str(abs(diff)) + ' plus vieux que moi.')
else: 
    if son_age > votre_age:
        print('Vous etes ' + str(abs(diff)) + ' plus jeune que moi.')
    else:
        print('Nous avons le meme age.')

### Exercice 1.3 

a = int(input('Entrer le nombre a : '))
b = int(input('Entrer le nombre b : '))
if a > b:
    print(str(a), ' est plus grand que ', str(b))
elif a < b:
    print(str(a), ' est plus petit que ', str(b))
else:
    print(str(a), ' est egal a ', str(b))

### Exercice 2.1

note = int(input('Entrer votre note (0-100) : '))
if note >= 90:
    print('A')
elif 70 < note < 89:
    print('B')
elif 60 < note < 69:
    print('C')
elif 50 < note < 59:
    print('D')
else:
    print('F')

### Exercice 2.2

mois = str(input('Entrer le mois en cours : ')).lower()
dict = {
    'septembre':'automne',
    'octobre':'automne',
    'novembre':'automne',
    'decembre':'hiver',
    'janvier':'hiver',
    'fevrier':'hiver',
    'mars':'printemps',
    'avril':'printemps',
    'mai':'printemps',
    'juin':'ete',
    'juillet':'ete', 
    'aout':'ete'
}

print(dict[mois])


for k in dict.keys():
    print(k,dict[k])
for k, v in dict.items():
    print(k,v)

##### Autre exemple

car = {
    'citroen' : 10000,
    'renault' : 11000,
    'audi' : 30000,
    'bmw' : 35000
}

my_car = str(input('Entrer votre marque de voiture : '))
print(car[my_car])

### Exercice 2.3

fruits = ['banana','orange','mango','lemon']
saisie = str(input('Entrer votre fruit : ')).lower()
if saisie != fruits:
    fruits.append(saisie)
else:
    print('Le fruit existe deja dans la corbeille.')

# Exercice 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][2])

if 'skills' in person:
    if 'Python' in person.values():
        print(person)

if ('skills',['JavaScript','React']) in person.items():
    print('He is a front end developer')
elif ('skills',['Node','Python','MongoDB']) in person.items():
    print('He is a back end developer')
elif ('skills',['React','Node','MongoDB']) in person.items():
    print('He is a fullstack developer')
else:
    print('Unknown title')

#if person['is_married']:
#if person['country'] == 'Finland':
if ('is_married', True) in person.items():
    if ('country', 'Finland') in person.items():
        print('Blablabla')

if ('is_married',True) in person.items() and ('country','Finland') in person.items():
    print('Great')

# Exercices_02.md

# Question 1

list = []
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        list.append(str(x))
print (','.join(list))

# Question 2

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print("Factoriel d'un negatif impossible")    
elif num == 0:    
   print("Le factoriel de 0 est 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("Le factoriel de",num,"est",factorial)
# A compléter avec le join

# Question 3

dict = {}
for i in range(1,11):
    dict[i] = pow(i,2) # i*i ou i**2 est possible
print(dict)

# Exercices_03.md
# Loops exercices

# Exercice 1.1
for i in range(0,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

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

# Exercices_04.md 
# Lists exercices

# Exercice 1

list = []
list = [1,2,3,4,5,6]
print(len(list)/2)
print(list[0],list[2],list[-1])

mixed_data_types = ['name','age','height','marital status','adress']
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))

print(it_companies[0],it_companies[3],it_companies[-1])
it_companies[0] = 'boobook'
print(it_companies)

it_companies.append('Netflix')
it_companies.insert(3,'Disney')
it_companies[1].upper()
'#; '.join(it_companies)

if 'Disney' in it_companies:
    print('Disney est dans la liste')

it_companies.sort()
it_companies.reverse()

it_companies[:3]
it_companies[-3:]
it_companies[3:-3]

it_companies.pop(0)
it_companies.pop(3)
it_companies.pop(-1)

it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end
full_stack.extend(back_end)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

# Exercice 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(min(ages))
print(max(ages))

ages.append(min(ages))
ages.append(max(ages))

import numpy as np
np.median(ages)

np.mean(ages)

etendue = max(ages) - min(ages)
print(etendue)

pays = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

pays_milieu = int(len(pays)/2)
print(pays[pays_milieu])

taille = int(len(pays))
list1 = []
list2 = []
if taille % 2 == 0: 
    list1 = pays[:taille//2]
    list2 = pays[taille//2:]
else:
    list1 = pays[:(taille//2)+1]
    list2 = pays[(taille//2)+1:]
    
print(list1)
print(list2)

print(abs(min(ages)-np.mean(ages)))
print(abs(max(ages)-np.mean(ages)))

payscut = []
paysscandi = []
payscut = pays[:3]
paysscandi = pays[3:]
print(payscut)
print(paysscandi)