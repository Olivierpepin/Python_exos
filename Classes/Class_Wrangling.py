# Creation de classe

class DataA:
    module = "Python"
    # attributs de class
    def __init__(self, nombre_exercices):  # __init__ est un constructeur
        self.nbr_exos = nombre_exercices

    def print_(self, param):
        print("Module :", self.module, " | Nombre d'exercices : ", self.nbr_exos, " ", param)
    
    def add(self):
        self.nbr_exos += 1
    # fonctions :
        # constructeur - attributs d'objet
        # autres fonctions de traitement

x = DataA(12)

x.add()

x.nbr_exos

x.module

x.print_(1)

y = DataA(21)

y.print_(1)

# Class methods avec utilisation de cls pour reference tous les objets. Appele avec le nom de la classe

@classmethod
def print_class_description(cls):
    print(cls.module)

# Static methods 

@staticmethod
def say_hello():
    print("Hello")

# Property methods

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    @property
    def float_value(self):
        return self.numerator/self.denominator
    
a = Fraction(1,3)
a.float_value

# Private attributes and methods start with a single underscore (_).
# These attributes and methods should only be accessed from within the class/object:

class SomeClass:
    def __init__(self):
        self._priv_attribute = 0
    def _priv_method(self):
        self._priv_attribute += 1

x = SomeClass()
# This is possible, but should not be done, as the attribute is defined as private
x._priv_attribute


# Ouverture de fichier avec Data Wranggling et envoi à un fichier

file = open("texte.txt", "r", encoding='utf-8')

lines = file.readlines()

lines_clean = []

for line in lines:
    if line != "\n":
        line = line.replace(".\n","")
        line = line.replace("\n","")
        lines_clean.append(line.split('.')[1])

print(" ".join(lines_clean))

f = open("text_complet.txt", "w", encoding='utf-8')
f.write(" ".join(lines_clean))
f.close()


# Pour json loads passe string en dictionnary et dumps passe dictionnary en string.