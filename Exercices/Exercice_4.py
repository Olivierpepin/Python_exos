# Exercices_04 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_04.md

# Lists Exercices

import numpy

# Exercice 1 - Level 1

# 1 Declare an empty list

list = []

# 2 Declare a list with more than 5 items

list = [1,2,3,4,5,6]

# 3 Find the length of your list

list = [1,2,3,4,5,6]

print(len(list))

# 4 Get the first item, the middle item and the last item of the list

list = [1,2,3,4,5,6]

print(len(list)/2)

print(list[0],list[2],list[-1])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['name','age','height','marital status','adress']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# 7 Print the list using print()

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies)

# 8 Print the number of companies in the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(len(it_companies))

# 9 Print the first, middle and last company

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies[0],it_companies[3],it_companies[-1])

# 10 Print the list after modifying one of the companies

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

it_companies[0] = 'HP'

print(it_companies)

# 11 Add an IT company to it_companies

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

it_companies.append('Netflix')

print(it_companies)

# 12 Insert an IT company in the middle of the companies list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

it_companies.insert(3,'Disney')

print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

compagnie_upper = it_companies[2].upper()

print(compagnie_upper)

# 14 Join the it_companies with a string '#;  '

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

'#;  '.join(it_companies)

# 15 Check if a certain company exists in the it_companies list.

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

if 'IBM' in it_companies:print('IBM est dans la liste')

# 16 Sort the list using sort() method

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

it_companies.sort()

print(it_companies)

# 17 Reverse the list in descending order using reverse() method

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

it_companies.reverse()

print(it_companies)

# 18 Slice out the first 3 companies from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies[:3])

# 19 Slice out the last 3 companies from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies[-3:])

# 20 Slice out the middle IT company or companies from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies[3:-3])

# 21 Remove the first IT company from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies.pop(0))

# 22 Remove the middle IT company or companies from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies.pop(3))

# 23 Remove the last IT company from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies.pop(-1))

# 24 Remove all IT companies from the list

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies.clear())

# 25 Destroy the IT companies list (not definied)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

del it_companies

print(it_companies)

# 26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end
full_stack.extend(back_end)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

# Exercice 2

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort

print(ages)

print(min(ages))
print(max(ages))

# Add the min age and the max age again to the list

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.append(min(ages))
ages.append(max(ages))

print(ages)

# Find the median age (one middle item or two middle items divided by two) median = 24

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

import numpy as np

np.median(ages)

# Find the average age (sum of all items divided by their number) mean = 22,8

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

np.mean(ages)

# Find the range of the ages (max minus min)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

etendue = max(ages) - min(ages)
print(etendue)

# Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

avg_min = abs(min(ages)-np.mean(ages))
avg_max = (max(ages)-np.mean(ages))

value = avg_min - avg_max

print(value)

# Find the middle country(ies) in the countries list

pays = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

pays_milieu = int(len(pays)/2)
print(pays[pays_milieu])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

pays = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

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

# Unpack the first three countries and the rest as scandic countries.

pays = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

taille = int(len(pays))
list1 = []
list2 = []
if taille % 2 == 0: 
    list1 = pays[:taille//2]
    list2 = pays[taille//2:]
else:
    list1 = pays[:(taille//2)+1]
    list2 = pays[(taille//2)+1:]

payscut = []
paysscandi = []
payscut = pays[:3]
paysscandi = pays[3:]
print(payscut)
print(paysscandi)