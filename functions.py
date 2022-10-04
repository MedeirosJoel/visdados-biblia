import json

from pkg_resources import working_set

removeCaracteres = ('.', ',', '!', '?', ':', ';', "{", "}", "(", ")")
stopedWords = ("NO", "NA", "O", "A", "E", "À", "ÀS", "DA", "SEM", "DE", "DAS", "DOS", "DO", "SE", "AS", "UM", "UMA", "UNS", "UMAS", "AO", "NA", "NOS", "MAS", "OS", "EM", "PARA", 'É', 'QUE', 'AOS')

def readJson(filepatch):
    file = open(filepatch, 'r')
    return json.load(file)

def cleanCaracteres(bible):
    
    bigString = ''
    versiclesList = []
    for book in bible:
        chapters = book["chapters"]
    
        for chapter in chapters:
            for versicle in chapter:
                count = 0
                listVersicle = list(versicle)

                for letter in listVersicle:

                    if letter in removeCaracteres:
                        listVersicle[count] = ''
                    else: pass   

                    count += 1

                versiclesList.append(''.join(listVersicle))

    bigString = ' '.join(versiclesList)

    return bigString.upper()

#Filter Function
def cleanStoppedWords(text):
    
    if text in stopedWords:
        flag = False
    else:
        flag = True
    
    return flag

