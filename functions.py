from collections import Counter
import csv
import json
import os

removeCaracteres = ('.', ',', '!', '?', ':', ';', "{", "}", "(", ")", "'", '"', '')
stopedWords = ('LHE', 'PORQUE', 'POR QUE', 'POR QUÊ', 'PORQUÊ' 'NO', 'NA', 'O', 'A', 'E', 'À', 'ÀS', 'DA', 'SEM', 'DE', 'DAS', 'DOS', 'DO', 'SE', 'AS', 'UM', 'UMA', 'UNS', 'UMAS', 'AO', 'NA', 'NOS', 'MAS', 'OS', 'EM', 'PARA', 'É', 'QUE', 'AOS', 'TAMBÉM', 'ENTÃO', 'FOI', 'POIS', 'COMO')

def readJson(version):
    filepatch = f"json/{version}.json"
    file = open(filepatch, 'r', encoding='UTF8')
    return json.load(file)

#Clean Caracteres and append Texts
def CleanCaracteres(bible):
    
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

def counterWordsaFile(bigCleanList, version, flag=False):
    
    countDict = Counter(bigCleanList)
    
    filepatch = f'csv/{version}.csv'
    os.remove(filepatch)

    with open(file=filepatch, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['word', 'count'])
        
        for key, value in countDict.items():
            writer.writerow([str(key), str(value)])
        
    if flag is True: output = countDict
    else: output = None
    
    return output 