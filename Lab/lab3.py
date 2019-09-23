# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:09:31 2019

@author: nithish k
"""

## Questions 1

def merge(leftList, rightList):
    mergedList = []
    leftLen = len(leftList)
    rightLen = len(rightList)
    i = j = 0
    
    while(i < leftLen and j < rightLen):
        
        if (leftList[i] <= rightList[j]):
            
            mergedList.append(leftList[i])
            
           
            i+=1
        
        else :
            mergedList.append(rightList[j])
           
            j +=1

    while(i < leftLen):
        mergedList.append(leftList[i])
        
        i+=1
    
    while(j < rightLen):
        
         mergedList.append(rightList[j])
         
         j+=1
         
         
    return mergedList


def mergeSort(inpList):
    n = len(inpList)
    if (n <= 1):
        return inpList
    mid = int(n/2)
    leftList = mergeSort(inpList[0:mid])
    rightList =  mergeSort(inpList[mid:])
    return merge(leftList, rightList)


filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab3_test_sorting.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums
mergeSort(readFileToList(filePath))


def writeToFile(filename,listOfOutput):
    file = open(filename,"w") 
    for line in listOfOutput:
  # write line to output file
      file.write(line)
      file.write("\n")
    file.close()
    
writeToFile("Output.txt",mergeSort(readFileToList(filePath)))








