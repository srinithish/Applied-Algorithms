# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:23:34 2019

@author: nithish k
"""

import numpy as np


def maxSubString(stringA,stringB):
    
    DPMatrix = [[(0,[]) for i in range(len(stringB)+1)] for j in range(len(stringA)+1)]
    
    for i in range(len(stringA)):
        for j in range(len(stringB)):
            
            if i+1 < len(DPMatrix) and j+1 < len(DPMatrix[0]) :
                
                Di,Dj = i+1,j+1
                matched = (-1,[])
                goBackOnJ = (-1,[])
                goBackOnI = (-1,[])

                if stringA[i] == stringB[j]:
                    matched = (DPMatrix[Di-1][Dj-1][0] + 1, DPMatrix[Di-1][Dj-1][1]+[(i,j)])
                else:
                    goBackOnJ = (DPMatrix[Di][Dj-1][0],  DPMatrix[Di][Dj-1][1])
                    goBackOnI = (DPMatrix[Di-1][Dj][0], DPMatrix[Di-1][Dj][1])
                    
                DPMatrix[Di][Dj] = max(matched,goBackOnJ,goBackOnI)
            
    
    return DPMatrix



filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab9_test_lcs.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >=0 :
            listOfNums.append(line.strip("\n"))
    
    file.close()
    return listOfNums      

          
listOfStrings = readFileToList(filePath)

DPMatrix = maxSubString(listOfStrings[0],listOfStrings[1])
print("Num macthing string is ",DPMatrix[-1][-1][0] )

commonChars = []
for tup in DPMatrix[-1][-1][1]:
   commonChars.append(listOfStrings[0][tup[0]])
print("".join(commonChars))
