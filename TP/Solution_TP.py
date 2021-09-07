# Tp Cours Python from : https://github.com/ElMehdiBen/Py_Course/tree/main/TP

# You can search by number with # (ie : # 1, # 3)

## 1 Create a class called "TextProcessing" with an init function (constructeur) that takes a text as input to create the object.

class TextProcessing:
    def __init__(self, text):
        self.text = text


## 2 In the same class : Create a function that counts the number of times 
## a word given as a parameter was used in the object TextProcessing

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0                               # Demarrage de la phase de cleaning
        # Il est possible d'utiliser un \ afin de faire continuer notre code sur plusieurs lignes.
        # Il ne faut pas de caractères après le \ (même un espace). Il y a donc qu'une seule ligne ici.
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")      # Il y a conflit sur les " avec celle à l'intérieur.
        for e in text.split(" "):               # Il est possible d'utiliser un \ (escape) et l'IDE ne l'intrepretera pas.
            if e.lower() == word.lower():
                count += 1
        return count

file_1 = open("obama_speech.txt", "r", encoding='utf-8') # Ouverture du fichier en lecture avec un encodage utf-8
text_1 = file_1.read()                                   # Lecture du fichier et attibution a text_1

obama = TextProcessing(text_1)                           # Definition de l'objet obama avec le texte en classe

print(obama.word_occurences("it")) # recherche du nombre d'occurence de it


## 3 In the same class : Create a function that counts the number of pharagraphs in the object TextProcessing

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):                    # Un paragrapge est défini comme un texte terminant pas un "."
        text = self.text.replace("...", " ") # Les ... ne constituent pas un paragraphe
        return len(text.split(".")) - 1 # Le dernier point va considérer un paragraphe. Il faut l'enlever (-1)

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

print(obama.paragraphs())


## 4 In the same class : Create a function that counts the number of lines in the object TextProcessing

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1 # Split sur les retours lignes (retour chariot en \n pour Microsoft)

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

print(obama.lines())


## 5 In the same class : Create a function that counts the number of words in the object TextProcessing

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1   # Split sur les retours lignes (retour chariot en \n pour Microsoft)
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))             # Applique le cleaning original. Split sur espace puis count.

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

print(obama.words())


## 6 In the same class : Create a function that returns a list of unique words used in the object TextProcessing

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))         # Utilisation d'un set (tuple) pour enlever les elements en double (rendre unique)

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

print(obama.uniques())


## 7 In the same class : Create a function that returns the intersection of unique words in two TextProcessing objects
## 7 correspond à 9 dans cet exemple comme nous appliquons directement aux fichiers obama_speech.txt et donald_speech.txt

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))
    
    def intersection_(self, other):
        uniques_1 = self.uniques()
        uniques_2 = other.uniques()
        # set_1.intersection(set_2)
        # intersectionn(list_1, list_2)
        return list(uniques_1.intersection(uniques_2)) # renvoi les mots identiques de 2 textes differents dans une liste.

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)


file_2 = open("donald_speech.txt", "r", encoding='utf-8') # Ajout du deuxième texte
text_2 = file_2.read()

donald = TextProcessing(text_2)


print(obama.intersection_(donald)) # print selon la méthode set_1.intersection(set_2)


## 8 Read the file obama_speech.txt and apply the functions 2 to 6 and then save the results to a new text file

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))         # Suppression de l'intersection comme fonction 2 a 6


file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

results = open("results.txt", "a")          # Ouverture du fichier results.txt en ecriture. "a" pour à la suite. "w" pour replace
results.write("Result Obama : \n")          # Il est possible de placer des \n au début des params pour envoyer à la ligne
results.write("Occurences de IT : " + str(obama.word_occurences("it")) + "\n")
results.write("Number de Paragraphs: " + str(obama.paragraphs()) + "\n")
results.write("Number of Lines : " + str(obama.lines()) + "\n")
results.write("Number of Words : " + str(obama.words()) + "\n")
results.close()                               # Fermeture du fichier

# Il est possible d'ecrire l'integralite des write sur une seule ligne

# result_text = "Resultats :\nNombre de paragraphes : " + str(obama.paragraphs()) + "\nNombre de lignes : " + str(obama.lines()) + "\nNombre de mots : " + str(obama.words())


## 9 Read the file donald_speech.txt and apply the functions 7 to get its words intersection with obama_speech.txt
## Identique à 7.

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))
    
    def intersection_(self, other):
        uniques_1 = self.uniques()
        uniques_2 = other.uniques()
        # set_1.intersection(set_2)
        # intersectionn(list_1, list_2)
        return list(uniques_1.intersection(uniques_2)) # renvoi les mots identiques de 2 textes differents dans une liste.

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)


file_2 = open("donald_speech.txt", "r", encoding='utf-8') # Ajout du deuxième texte
text_2 = file_2.read()

donald = TextProcessing(text_2)


print(obama.intersection_(donald)) # print selon la méthode set_1.intersection(set_2)


## 10 Use the results from 9 and apply function 2 on each of word 
## in both speeches to compare the use of words by Obama and Donald

class TextProcessing:
    def __init__(self, text):
        self.text = text

    def word_occurences(self, word):
        count = 0
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", " ")\
                        .replace("\"", "")
        for e in text.split(" "):
            if e.lower() == word.lower():
                count += 1
        return count
    
    def paragraphs(self):
        text = self.text.replace("...", " ")
        return len(text.split(".")) - 1

    def lines(self):
        return len(self.text.split("\n")) - 1
    
    def words(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return len(text.split(" "))
    
    def uniques(self):
        text = self.text.replace(",", " ")\
                        .replace(":", " ")\
                        .replace(";", " ")\
                        .replace("- ", "")\
                        .replace("...", " ")\
                        .replace(".", "")\
                        .replace("  ", " ")\
                        .replace("  ", " ")\
                        .replace("\n", "")\
                        .replace("\"", "")
        return set(text.split(" "))
    
    def intersection_(self, other):
        uniques_1 = self.uniques()
        uniques_2 = other.uniques()
        # set_1.intersection(set_2)
        # intersectionn(list_1, list_2)
        return list(uniques_1.intersection(uniques_2))

file_1 = open("obama_speech.txt", "r", encoding='utf-8')
text_1 = file_1.read()

obama = TextProcessing(text_1)

file_2 = open("donald_speech.txt", "r", encoding='utf-8') 
text_2 = file_2.read()

donald = TextProcessing(text_2)

inter = obama.intersection_(donald) # definition d'une variable intersection

for term in inter:
    print("Obama used : ", term, " ", obama.word_occurences(term), " times")
    print("Trump used : ", term, " ", donald.word_occurences(term), " times")
    print("=======================")

