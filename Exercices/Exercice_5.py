# Exercice GITHUB https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_05.md

## Exercice 5 Level 0

# 1 Create an empty dictionary called dog

dog = {}
print(dog)



# 2 Add name, color, breed, legs, age to the dog dictionary

dog = {"name":"", "color":"", "breed":"", "legs":"", "age":""}
print(dog)


# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary

student = ["first_name", "last_name", "gender", "age", "marital status", "skills", "country", "city", "address"]
dict_student = dict.fromkeys(student)

print(student)


# 4 Get the length of the student dictionary

student = ["first_name", "last_name", "gender", "age", "marital status", "skills", "country", "city", "address"]
dict_student = dict.fromkeys(student)

print(len(dict_student))


# 5 Get the value of skills and check the data type, it should be a list

student = ['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'address']

dict_student = dict.fromkeys(student)

dict_student['skills']=['english','math']

print(dict_student['skills'])

print(type(dict_student))


# 6 Modify the skills values by adding one or two skills

liste = ['first_name','last_name','gender','age','marital_status','skills','country','city','adress']

student = dict.fromkeys(liste)

student['skills'] = ['maths','francais','histoire','science']

student['skills'] += ['EPS']

print(student['skills'])

print(student)


# 7 Get the dictionary keys as a list

a_dict = {"a": 1, "b": 2, "c": 3}

list(a_dict.keys())


# 8 Get the dictionary values as a list

a_dict = {"a": 1, "b": 2, "c": 3}

list(a_dict.values())


# 9 Change the dictionary to a list of tuples using items() method

a_dict = {"a": 1, "b": 2, "c": 3}

list_a_dict = list(a_dict.items())
print(list_a_dict)


# 10 Delete one of the items in the dictionary

a_dict = {"a": 1, "b": 2, "c": 3}

del a_dict['a']
print(a_dict)


# 11 Delete one of the dictionaries

a_dict = {"a": 1, "b": 2, "c": 3}

a_dict.clear()
print(a_dict)


# Exercises: Level 1

# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    x = a + b
    return x

add_two_numbers(1,2)


# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def aoc(r):
    aire = 3.14 * r * r
    return aire

aoc(3)


# 3 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def cel(r):
    f = (r * 9/5) + 32
    return f

cel(15)


# 4 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

# With locals variables

def season(r):
    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']
    if r in Autumn:
        print('The season is Autumn')
    elif r in Winter:
        print('The season is Winter')
    elif r in Spring:
        print('The season is Spring')
    elif r in Summer:
        print('The season is Summer')
    else:
        print('This is not a month')

season('March')

# With globals variables

Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

def season(r):
    if r in Autumn:
        print('The season is Autumn')
    elif r in Winter:
        print('The season is Winter')
    elif r in Spring:
        print('The season is Spring')
    elif r in Summer:
        print('The season is Summer')
    else:
        print('This is not a month')

season('October')


# 5 Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,y1,x2,y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1     
    return a,b

calculate_slope()


# 6 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list. (surdefinition)

Tlist=[26,8,3]

def print_list(liste):
    print(liste)

print_list(Tlist)

# Avec loop

def print_list(liste):
    for i in liste:
        print(i)


# 7 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# Without loop

def reverse_list(liste):
    liste2 = liste[::-1]
    return liste2

Tlist=[26,8,3]

reverse_list(Tlist)

# With loop

def reverse_list(liste):
    i=len(liste)-1
    rlist = []
    while i > -1:
        rlist.append(liste[i])
        i-=1
    print(rlist)

Tlist=[26,8,3]

reverse_list(Tlist)

loto = [2,45,12,58,12]
def reverse_list(array):
    listerev = []
    for i in range(len(array)-1,-1,-1):
        listerev.append(array[i])
    print(listerev)
reverse_list(loto)


# 10 Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items

Tlist= ["Marc", "lavoine"]

def capitalize_list_items(liste):
    for i in range(len(liste)):
        liste[i] = liste[i].upper()
    return liste

capitalize_list_items(Tlist)


# for i in x

Tlist= ["Marc", "lavoine"]

def capitalize_list_items(liste):
    liste2 = []
    for i in liste:
        liste2.append(i.upper())
    return liste2

capitalize_list_items(Tlist)


minuscule = ['je','suis','ecrit','en','minuscule']

def capitalize_list_items(liste):
    for i in range(len(liste)):
        liste[i].upper()
    print(liste)

capitalize_list_items(minuscule)


def cli(l):
    L=[]
    for i in l:
        #On modifie la valeur de i avant de l'insérer dans la liste
        i=i.upper()
        L.append(i)
    return(L)

Test=['allo','aled','sovémwa']

cli(Test)


# 11 Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end.

Tlist=[26,8,3]

# fonction lambda l.extend([x for i in range(100)])

def add_item(x,y):
    x.append(y)
    return x

add_item(Tlist,15)


# 12 Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.

Tlist=[26,3,8,5,3]

def remove_item(x,y):
    x.remove(y)
    return x

remove_item(Tlist,3)


# 13 Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.

def sum_of_number(n):
    j = 0
    for i in range(1,n+1):
        j += i
    return j

sum_of_number(5)


# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    j = 0
    for i in range(1,n+1):
        if (i%2) == 1:
            j += i
    return j

sum_of_odds(5)


# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

def sum_of_even(n):
    j = 0
    for i in range(1,n+1):
        if (i%2) == 0:
            j += i
    return j

sum_of_even(5)


# Exercice Level 2

# 1 Declare a function named evens_and_odds . It takes a positive integer as parameter 
# and it counts number of evens and odds in the number.

def evens_and_odds(i):
    sum_even = 0
    sum_odd = 0
    for i in range(0,i+1):
        if (i%2) == 0:
            sum_even += 1 
        else:
            sum_odd += 1
    print('La somme des nombres paires est', sum_even)
    print('La somme des nombres impaires est', sum_odd)

evens_and_odds(100)


# 1.1 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(i):
    factorial = 1
    if i < 0:
        print("Factoriel d'un negatif impossible")
    elif i == 0:
        print("Le factoriel de 0 est 1")
    else:    
        for i in range(1,i+1):
            factorial = factorial*i
        print("Le factoriel de",i,"est",factorial)

factorial(8)


# 2 Call your function is_empty, it takes a parameter and it checks if it is empty or not

# https://www.kite.com/python/answers/how-to-check-if-a-variable-is-empty-in-python


def is_empty(x):
    is_non_empty = bool(x)
    print(is_non_empty)

is_empty("")


# 3 Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

# Import librairie statistics

import statistics

# mean

Test_list = [1,3,5,27,158]

def calculate_mean(list):
    x = statistics.mean(list)
    return x

calculate_mean(Test_list)

# median

import statistics

Test_list = [1,3,5,27,158]

def calculate_median(list):
    x = statistics.median(list)
    return x

calculate_median(Test_list)

import statistics

# mode 

Test_list = [1,3,5,27,158,3,3]

def calculate_mode(list):
    x = statistics.mode(list)
    return x

calculate_mode(Test_list)

# range

Test_list = [1,3,5,27,158,25]

def calculate_range(list):
    x = len(list)
    return x

calculate_range(Test_list)

# variance

import statistics

Test_list = [1,3,5,27,158,25]

def calculate_variance(list):
    x = statistics.variance(list)
    return x

calculate_variance(Test_list)

# standard deviation

import statistics

Test_list = [1,3,5,27,158,25]

def calculate_std(list):
    x = statistics.stdev(list)
    return x

calculate_std(Test_list)


# Exercice Level 3

# 1 Write a function called is_prime, which checks if a number is prime.

# Prime number : https://www.w3resource.com/python-exercises/python-functions-exercise-9.php

def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

is_prime(5)


# 2 Write a function which checks if all items are unique in the list.

tlist = [3,4,56,75,45,1,1]

def unique(test_list):
    if len(set(test_list)) == len(test_list):
        flag = 1
    else:
        flag = 0 
    return flag

unique(tlist)

# avec fonction bool

tlist = [3,4,56,75,45,1,1]

def unique(test_list):
    x = len(set(test_list)) == len(test_list)
    x = bool(x)
    print(x)

unique(tlist)


# 3 Write a function which checks if all the items of the list are of the same data type.

# https://stackoverflow.com/questions/13252333/check-if-all-elements-of-a-list-are-of-the-same-type

# 'Long' doesn't exist anymore in Python 3

tlist = [1,2,3]
flist = [1, "Potent", 5.23]

def checkInt(l):
    return all((isinstance(i, (int)) for i in l))

checkInt(tlist)


# 4 Write a function which check if provided variable is a valid python variable

# Need rework. Doesn't work for type object, builtin function or method

def valid_variable(x):
    a = x.isidentifier()
    return a

valid_variable(list)














