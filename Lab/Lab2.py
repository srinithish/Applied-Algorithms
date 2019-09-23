# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:32:41 2019

@author: nithish k
"""

###


def getMinNumber(listOfNums, startPos, endPos):
    tempMin = float("Inf")
    MinNumPos = -1
    for position,num in enumerate(listOfNums[startPos:endPos]):
        
        if num < tempMin:
            
            
            tempMin = num
            MinNumPos = position+startPos
            
        
    return MinNumPos,tempMin

def swap(ListOfNum, pos1, pos2):
    
    temp = ListOfNum[pos2]
    ListOfNum[pos2] = ListOfNum[pos1]
    ListOfNum[pos1] = temp
    
    return True

def selectionSort(ListOfNums):
    totLen = len(ListOfNums)
    for position, number in enumerate(ListOfNums):
        
        MinNumPos,restMinNum = getMinNumber(ListOfNums,position,totLen)
        swap(ListOfNums,position,MinNumPos)
             
        
        
    
# insertion sort


def insertionSort(ListOfNum):
    
    totalNums = len(ListOfNum)
    
    for i in range(1, totalNums):
        
        numberToCheck = ListOfNum[i]
        
        j = i-1
        
        while(j>=0 and ListOfNum[j]>numberToCheck):
            ListOfNum[j+1] = ListOfNum[j]
            j  = j - 1
        
        ListOfNum[j+1] = numberToCheck
        
    return True

#


filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/Lab2_test_sorting.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums


def writeToFile(filename,listOfOutput):
    file = open(filename,"w") 
    for line in listOfOutput:
  # write line to output file
      file.write(line)
      file.write("\n")
    file.close()


listOfNums = readFileToList(filePath)

selectionSort(listOfNums)

listOfNums = readFileToList(filePath)
insertionSort(listOfNums)

listOfNums =list( map(str,listOfNums))

writeToFile("Output.txt",listOfNums)



    

    
