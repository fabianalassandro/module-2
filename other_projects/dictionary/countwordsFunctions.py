#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:37:11 2019

@author: Fabiana
"""


#Creation of the list of stop words to compare with the dictionary
stopWords = []

def readStopWords():
    filepath = "textData/stopwords.txt"
    with open(filepath) as fp:
        for word in (fp): 
            stopWords.append(word.strip())
    return stopWords    
            
readStopWords()
#print(readStopWords())



# Creation of the dictionary where I'll list the words contained in the text
dictionary = {}

def countWords(stopWords):
    filepath = "textData/mobypara.txt"
    with open(filepath) as fp:
        line = fp.readline()
        countAllwords = 0
        for line in (fp):
#           print(line)
           words = line.split()
           for word in words:
#               print(word)
               countAllwords += 1
               if word not in stopWords:
                  
                   if word in dictionary:
                      dictionary[word] += 1
                   else:
                       dictionary["{}".format(word)] = 1 
    return dictionary       
countWords(stopWords)      

#print(dictionary, len(dictionary))

#Print the top 20 popular words
def printTop20():
    ranking = sorted(dictionary.items(), key=lambda kv: kv[1],reverse=True)
    print(ranking[0:21])
#printTop20()    


def testReading():
    stops = []
    filepath = open("textData/stopwords.txt")
    for word in filepath: 
            stops.append(word.strip())
#    print(stops)  
    filepath.close()       
testReading()


# Check for similarity


def createDictionary(filename):
    dictionaryText = {}
    filepath1 = open(filename)
    for line in filepath1:
        words = line.split()
        for word in words:
            if word not in stopWords:
                if word in dictionaryText:
                    dictionaryText[word] += 1
                else:
                    dictionaryText["{}".format(word)] = 1
    
    filepath1.close() #to close the file opened before  
    return dictionaryText

george01 = createDictionary("textData/george01.txt")
#print(george01)
#print()
print(len(george01))

george02 = createDictionary("textData/george02.txt")
#print(george02) 
#print()

print(len(george02))

george03 = createDictionary("textData/george03.txt")
#print(george03)
#print() 

print(len(george03))   

george04 = createDictionary("textData/george04.txt")
#print(george04)
#print()

print(len(george04))


def compareWords(dict1, dict2):
    count = 0
    for word in dict1:
            if word in dict2:
                count += 1
                
                
    return count 
           
george1and2 = compareWords(george01, george02)

george1and3 = compareWords(george01, george03)

george1and4 = compareWords(george01, george04)

george2and3 = compareWords(george02, george03)

george2and4 = compareWords(george02, george04)

george3and4 = compareWords(george03, george04)

print()
print(george1and2)

print(george1and3)

print(george1and4)

print(george2and3)

print(george2and4)

print(george3and4)


# Check words in common between dictionaries and 

def similarity(wordsInCommon, total1, total2):
    totalWords = total1 + total2
    wordsNotInCommon = totalWords - wordsInCommon
    final = wordsInCommon / wordsNotInCommon
    return final

print()
print("1 and 2", round(similarity(george1and2, len(george01), len(george02)), 3))

print("1 and 3", round(similarity(george1and3, len(george01), len(george03)), 3))

print("1 and 4", round(similarity(george1and4, len(george01), len(george04)), 3))

print("2 and 3", round(similarity(george2and3, len(george02), len(george03)), 3)) 

print("2 and 4", round(similarity(george2and4, len(george02), len(george04)), 3))

print("3 and 4", round(similarity(george3and4, len(george03), len(george04)), 3))
    


    
    
    





