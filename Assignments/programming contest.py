# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:30:26 2019

@author: nithish k
"""

import math


def findSubset(index,totalSum,allElems,subsetDict, indexPath):
    
    if totalSum == 0 : ## if rest of totalSum is zero 
        return True 

    if index < 0 or totalSum < 0 :
        return False
  
        
    if (index,totalSum) not in subsetDict:
        subsetDict[(index,totalSum)] = max([findSubset(index-1,
                                                  totalSum-allElems[index],
                                                  allElems,subsetDict, indexPath),
                                            findSubset(index-1,totalSum,allElems,subsetDict, indexPath) ])
          
            
        

        
    return subsetDict[(index,totalSum)]
    



def getBestPossibleDiff(numElems, listOfWeights):
    
    
    
    totalWeight = sum(listOfWeights)
    
    halfWeight = int(math.ceil(totalWeight/2))
#    halfWeight = int(totalWeight/2)
    difference = []
    for possSum in range(halfWeight,-1,-1):
        subsetDict = {}
        indexPath = []
        
        
        if findSubset(numElems-1,possSum,listOfWeights,subsetDict, indexPath) == True:
            
#            diff  = max([(totalWeight - possSum)-possSum,possSum-(totalWeight - possSum)])
            diff  = max([(totalWeight - possSum) - possSum ,  possSum - (totalWeight - possSum)]) 
#            return diff
#            difference.append(diff)
            return diff
    
    
    return False
    
    

#
numElems = int(input())
listOfWeights = input()
listOfWeights = [int(i) for i in listOfWeights.split()]
print(getBestPossibleDiff(numElems,listOfWeights))
    
#print(getBestPossibleDiff(5,[1,5,2,10,3]))


