# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:33:51 2019

@author: nithish k
"""
import random
import time


def generateRandomNumbers(listOfRandNums, numNumbers):
    random.seed(int(time.time()))
    
    for i in range(numNumbers):
        
        listOfRandNums.append(random.randint(0,100)/100)

myList = []
generateRandomNumbers(myList, 20)


def swap(ListOfNum, pos1, pos2):
    
    temp = ListOfNum[pos2]
    ListOfNum[pos2] = ListOfNum[pos1]
    ListOfNum[pos1] = temp
    
    return True



def quickSort(ListToSort,start, end):
    
    if start < end:
    
        index = random.randint(start,end-1)
        
        swap(ListToSort,start,index)
        
        indexOfPivotPlace = partition(ListToSort,start,end)
        quickSort(ListToSort,start,indexOfPivotPlace)
        quickSort(ListToSort,indexOfPivotPlace+1,end)
    
   
            


def partition(ListToPartition,start,end):
    
    
    leftSideCount = start+1
    rightSideCount = end-1
    
    pivot = ListToPartition[start]
    
    while(leftSideCount<=rightSideCount):
        
        while(leftSideCount<=rightSideCount and ListToPartition[leftSideCount] <= pivot):
            
            leftSideCount+=1
        
        while(leftSideCount<=rightSideCount and ListToPartition[rightSideCount]>=pivot):
            rightSideCount-=1
        
        if(leftSideCount<rightSideCount):
            
           swap(ListToPartition,leftSideCount,rightSideCount)

    swap(ListToPartition, start, rightSideCount)
    
    
    return rightSideCount
    
    
filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab4_test_sorting.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >=2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums



myList = readFileToList(filePath)
quickSort(myList,0,len(myList)-1)
    
    
    
    
    
    
    
    
    