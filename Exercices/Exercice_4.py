# Exercices_04 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_04.md

# Lists Exercices

import numpy

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

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

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