# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:37:10 2019

@author: Srinithish k
Lab 1 Assignment
"""

#load the array from text file

filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab1_minNumber_test.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums


listOfNums = readFileToList(filePath)



def getMinNumber(listOfNums, startPos, endPos):
    tempMin = float("Inf")
    for num in listOfNums[startPos:endPos+1]:
        if num < tempMin:
            tempMin = num
    
    return tempMin



outputList = [getMinNumber(listOfNums,0,99),getMinNumber(listOfNums,100,399),getMinNumber(listOfNums,400,999)]
##Qyestion 1 minnumber from 0 to 99 index
print(getMinNumber(listOfNums,0,99)) #7

##Q2 min number form 100 to 399 index
print(getMinNumber(listOfNums,100,399)) #3

##Q2 min number form 400 to 999 index
print(getMinNumber(listOfNums,400,999)) #0



