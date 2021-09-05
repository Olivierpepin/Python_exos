# Exercices_02 from https://github.com/ElMehdiBen/Py_Course/blob/main/Exercices_02.md

# Question 1 - Level 1

## Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
## between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

## Consider use range(#begin, #end) method.


reponse=list()

for x in range(2000, 3201):
    # Numbers that 7 divisable 7 but not 5
    if x % 7 == 0 and x % 5 != 0:
        reponse.append(x)
print(reponse)



# Function with list included. Not single line.

reponse=list()

def number():
    reponse=list()
    for x in range(2000, 3201):
        # Numbers that 7 divisable 7 but not 5
        if x % 7 == 0 and x % 5 != 0:
            reponse.append(x)
    return reponse

number()


# Question 2 - Level 2

## Write a program which can compute the factorial of a given numbers.
## The results should be printed in a comma-separated sequence on a single line.
## Suppose the following input is supplied to the program: 8 Then, the output should be:40320

## In case of input data being supplied to the question, it should be assumed to be a console input.


n=int(input("Input a number to compute the factiorial : "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(n)

# Refactorise without else type

n = int(input("Input a number to compute the factiorial : "))

def factorial(n):
    x = 1
    if n != 0: x = n * factorial(n-1)
    return x

factorial(n)


# Question 3 - Level 3

## With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included),
## and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

## Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 

## Hints : In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict() (dictionnary)


number = int(input("Type a number: "))

numberDict = {}

for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)

# With function

def dict(i):
    for i in range(1, i+1):
        numberDict[i] = i*i
    print(numberDict)

dict(8)





