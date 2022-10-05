from threading import Thread
from time import sleep, time
from functions import *

initTime = time()

versions = ("nvi", "acf", "aa")
process = []

def runThread(version, flag=False):
    print(f"Thread: {version} inciado em: {time()-initTime:.2f}s")

    filepatch = f"json/{version}.json"
    bible = readJson(filepatch)
    
    bigString = cleanCaracteres(bible)
    bigList = bigString.split(' ')
    
    filterList = filter(cleanStoppedWords, bigList)
    bigCleanString = ' '.join(filterList)
    
    file = open(f"txt/{version}.txt", 'w', encoding='UTF8')
    file.write(bigCleanString)
    file.close()
    
    print(f"Thread: {version} finalizado em: {time()-initTime:.2f}s")
    
    if flag is True:
        return bigCleanString
    else:
        return None

if "__main__" == __name__:
    for version in versions:
        tempThread = Thread(target=runThread, name=version, args=(version,))
        process.append(tempThread)
        process[-1].start()