from operator import index
from time import sleep, time
from functions import *
initTime = time()

versions = ("nvi", "acf", "aa")

version = "aa"
filepatch = f"json/{version}.json"
bible = readJson(filepatch)
bigString = cleanCaracteres(bible)
bigList = bigString.split(' ')
filterList = filter(cleanStoppedWords, bigList)
bigCleanString = ' '.join(filterList)

endTime = time()
print(endTime-initTime)

