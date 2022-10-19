from threading import Thread
from time import sleep, time
from functions import *

initTime = time()

versions = ("nvi", "acf", "aa")
process = []

def runThread(version, flag=False):
    print(f"Thread: {version} inciado em: {time()-initTime:.2f}s")

    bible = readJson(version) #Carrega o arquivo json, e entrega um objeto json
    
    bigString = CleanCaracteres(bible) #Organiza e limpa os
    bigList = bigString.split(' ')
    
    filterList = filter(cleanStoppedWords, bigList)
    bigCleanString = ' '.join(filterList)


    counterWordsaFile(bigCleanString.split(' '), version)
    filepatchtxt = f"txt/{version}.txt"
    os.remove(filepatchtxt)
    file = open(filepatchtxt, 'w', encoding='UTF8')
    file.write(bigCleanString)
    file.close()
    
    print(f"Thread: {version} finalizado em: {time()-initTime:.2f}s")
    
    result = None
    if flag is True: result = bigCleanString
    
    return result

if "__main__" == __name__:
    for version in versions:
        tempThread = Thread(target=runThread, name=version, args=(version, True,))
        process.append(tempThread)
        process[-1].start()