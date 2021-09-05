# Exercices_01 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_01.md

# Conditionals exercises

# Exercise 1.1 Get user input using input(“Enter your age: ”).
## If user is 18 or older, give feedback: You are old enough to drive. 
## If below 18 give feedback to wait for the missing amount of years.

saisie = input('Entrer votre age : ') # Saisie d'une variable en String

saisie_int = int(saisie) # Transformation variable saisie string en une variable integer
if saisie_int >= 18:
    print('Tu es assez agé pour apprendre a conduire.')
else:
    diff = 18 - saisie_int 
    # Retranformation variable integer en string pour concatenation
    print('Tu dois attendre ' + str(diff) + ' annee(s) pour apprendre a conduire.') 


# Exercise 1.2 Compare the values of my_age and your_age using if … else.
## Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
## You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
## and a custom text if my_age = your_age.


# With if / else (years difference not supported)

your_age = int(input('Entrer your age : ')) # Transformation directe des varibles string en integer
my_age = int(input('Entrer my age : '))

diff = my_age - your_age

if your_age < my_age:
    print('Vous etes ' + str(abs(diff)) + ' ans plus jeune que moi.')
else: 
    if your_age > my_age:
        print('Vous etes ' + str(abs(diff)) + ' ans plus vieux que moi.')
    else:
        print('Nous avons le meme age.')


# With elif (years implemented)

my_age = int(input("Enter my age : "))
your_age = int(input("Enter your age : "))

diff_age = my_age - your_age

year_label = "year"
if abs(diff_age) > 1:
    year_label = year_label + "s"

if diff_age > 0:
    print("You're",diff_age, year_label, "younger than me")
elif diff_age == 0:
    print("We have the same age")
else:
    print("You're",abs(diff_age), year_label, "older than me")


# Exercice 1.3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
## if a is less b return a is smaller than b, else a is equal to b.

a = int(input('Entrer le nombre a : '))
b = int(input('Entrer le nombre b : '))

if a > b:
    print(str(a), 'est plus grand que', str(b))
elif a < b:
    print(str(a), 'est plus petit que', str(b))
else:
    print(str(a), 'est egal a', str(b))
