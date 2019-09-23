# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:49:39 2019

@author: nithish k
"""

##insertion sort

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


myList = [31,41,59,26,41,58]
insertionSort(myList)
    



###problem 2

def unknown(ListOfNum):
    totalNums = len(ListOfNum)
    for i in range(totalNums-1):
        if ListOfNum[totalNums-1] < ListOfNum[i]:
            temp = ListOfNum[i]
            ListOfNum[i] = ListOfNum[totalNums-1]
            ListOfNum[totalNums-1] = temp
            
            
    return ListOfNum[totalNums-1]


unknown(myList)
        
"""
##problem 3
"""





inputListOfLists = [[1,3,5,7,9,11],[2,4,6,8,9,11],[4,5,6,7,9,11]]
k = 3
listOfCurrentIndices = [0 for i in range(k)]

for i in range(len(inputListOfLists[0])+10): ##running N
    tempMax = -float("Inf")
    for position,eachIndex in enumerate(listOfCurrentIndices):
        if eachIndex >= len(inputListOfLists[0]):
            break
        
        else:
            ### get maximum positions
            
            if inputListOfLists[position][eachIndex] > tempMax :
                tempMax = inputListOfLists[position][eachIndex]
    sameNumCount = 0            
    for position,eachIndex in enumerate(listOfCurrentIndices):          
     ## increasse the indicies here   
     
         if inputListOfLists[position][eachIndex] != tempMax:
             listOfCurrentIndices[position] +=1
         if inputListOfLists[position][eachIndex] == tempMax:
             sameNumCount += 1
    if sameNumCount == k:
        print(tempMax)



"""
problem 3 O(2*k*N-1)
"""
def findCommonElements(inputListOfLists):
#    inputListOfLists = [[1,3,5,7,9,11],[2,4,6,8,9,11],[4,5,6,7,9,11]]
#    k = 3
#    N = len(inputListOfLists[0])
    oldIntersectionList = inputListOfLists[0]
    
    for nextList in inputListOfLists[1:] :
        newIntersectionList = []
        indexIntersection = 0
        indexNextList = 0
        LenI = len(oldIntersectionList)
        LenJ = len(nextList)
        while(indexIntersection < LenI and indexNextList < LenJ):
            if oldIntersectionList[indexIntersection] == nextList[indexNextList]:
                newIntersectionList.append(oldIntersectionList[indexIntersection])
                indexIntersection += 1
                indexNextList += 1
                
                
            elif oldIntersectionList[indexIntersection] > nextList[indexNextList]:
                indexNextList += 1
                
            elif oldIntersectionList[indexIntersection] < nextList[indexNextList]:
                indexIntersection +=1
        oldIntersectionList = list(newIntersectionList)
    
    return oldIntersectionList

    






"""

##probelm 4


"""    

def find2MissingNums(inpList):
    ##trails
    numMissing = 2
    inpList.extend([-1 for i in range(numMissing)]) ##denoting empty spaces by -1
    emptyUsedCount = 0
    
    for position,value in enumerate(inpList):
        if inpList[value] != value and value != -1:
            temp1 = inpList[value]
            
            inpList[value] = value
            if emptyUsedCount <= numMissing:
                if inpList[-2] == -1: ##first slot is empty
                    inpList[-2] = temp1
                    emptyUsedCount += 1
                    inpList[position] = -1
                
                elif inpList[-1] == -1 : ##second slot is empty 
                    inpList[-1] = temp1
                    emptyUsedCount += 1
                    inpList[position] = -1
            else:
                inpList[position] = temp1
    
    ##print all the missing numbers            
    for i,value in enumerate(inpList):
        if value == -1: ##missing
            print(i)        



myList = [2,3,0,4,5]
find2MissingNums(myList)

"""
Problem 4
"""
def find2MissingNums(inpList):
    ##trails
    numMissing = 2
    inpList.extend([-1 for i in range(numMissing)]) ##denoting empty spaces by -1
   
    
    for position,value in enumerate(inpList):
        while position != value and value != -1:
            temp1 = inpList[value]
            
            inpList[value] = value
            inpList[position] = temp1
            value = inpList[position] #updated value
    ##print all the missing numbers            
    for i,value in enumerate(inpList):
        if value == -1: ##missing
            print(i)        



myList = [0,1,2,3,4]
find2MissingNums(myList)

##Question 6



def getKthLargestElem(k,listM,listN):
    ##kth largest cannot exist beyond listM's first k elems and listN's first k elems
    if len(listM) == 0:
        return listN[k]
    elif len(listN) == 0:
        return listM[k]
    
    
    
    newListM = list(listM)
    newListN = list(listN)
    midElemIndexM = int(len(newListM)/2)
    midElemIndexN = int(len(newListN)/2)
    
    
    if k > midElemIndexM + midElemIndexN:
    
        if newListM[midElemIndexM] < newListN[midElemIndexN]:   
            
            return getKthLargestElem(k-midElemIndexM-1,newListM[midElemIndexM+1:],newListN)
        
        elif newListM[midElemIndexM] > newListN[midElemIndexN]:
            
            return getKthLargestElem(k-midElemIndexN-1,newListM,newListN[midElemIndexN+1:])
    
    
    elif k <= midElemIndexM+ midElemIndexN :
        if newListM[midElemIndexM] < newListN[midElemIndexN]:
        
            return getKthLargestElem(k,newListM,newListN[:midElemIndexN])
            
        elif newListM[midElemIndexM] > newListN[midElemIndexN]:
            return getKthLargestElem(k,newListM[:midElemIndexM],newListN)
            

        
    
getKthLargestElem(3,[1,2,3,4,5],[3,4,5,6,7])


def kthlargest(arr1, arr2, k):
    
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]
    
    arr1 = arr1[:k]
    arr2 = arr2[:k]
    
    mida1 = int(len(arr1)/2)
    mida2 = int(len(arr2)/2)
    if mida1+mida2<k:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kthlargest(arr1[mida1+1:], arr2, k-mida1-1)
    else:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1[:mida1], arr2, k)
        else:
            return kthlargest(arr1, arr2[:mida2], k)

kthlargest([1,2,3,4,5],[3,4,5,6,7],2)


import random
random.randint(-1,2)
[_ for i in range(2)]


import random

def permuteNumbers(listOfNums):
    lengthN = len(listOfNums)
    totalTransferredIndices = 0
    allIndexes = []
    emptyArray = ['EMPTY' for i in range(lengthN)]
    while totalTransferredIndices < lengthN :
        randomParentIndex = random.randint(0,lengthN-1)
#        print(randomParentIndex)
        if randomParentIndex not in allIndexes:
            allIndexes.append(randomParentIndex)
            randomEmptyIndex = random.randint(0,lengthN-1)
            if emptyArray[randomEmptyIndex] == 'EMPTY':
                emptyArray[randomEmptyIndex] = listOfNums[randomParentIndex]
                print(randomParentIndex,emptyArray)
                totalTransferredIndices+=1
    
            

permuteNumbers([1,2,3,4])
