# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:35:29 2019

@author: nithish k
"""

## pull the first element and then sift down

"""

Question 1
"""


def swap(pos1,pos2,listToBeAltered):
    temp = listToBeAltered[pos1]
    listToBeAltered[pos1] = listToBeAltered[pos2]
    listToBeAltered[pos2] = temp
    
    pass



def heapify(listToConvert, position):
    ##position form 1
    
    if 2*position+2 < len(listToConvert): ##index in range or there exists a child
        
        initParent = listToConvert[position] ##pos
        leftChild = listToConvert[2*position+1] ##2*pos
        rightChild = listToConvert[2*position+2]  ## 2*pos+1
        newPosition = position
        
        if  leftChild > initParent and   leftChild >rightChild: ##left child is the greatest
            swap(2*position+1,position,listToConvert) ##swap parent with right
            newPosition = 2*position+1
            
        
        elif  rightChild > initParent and rightChild > leftChild: ##right child is the greatest
            swap(2*position+2,position,listToConvert) ##swap parent with right
            newPosition = 2*position+2
        
        if newPosition != position:
            print(listToConvert)
            
            heapify(listToConvert, newPosition)
        
    
    pass


def extractMax(heapedList):
    maxElem = heapedList[0]
    heapedList[0] = heapedList[-1] 
    del heapedList[-1] 
    heapify(heapedList,0)
        
    return maxElem

def buildMaxHeap(listToConvert):
    ##from last but one layer of nodes do heapify
    lastPosition = len(listToConvert)-1
    
    for i in range(int(lastPosition/2 -1),0,-1):
        heapify(listToConvert,i)

myList = [15, 5, 9,13, 12, 8, 7, 4, 0, 6, 2, 1]


extractMax(myList)


"""
[13, 1, 9, 5, 12, 8, 7, 4, 0, 6, 2]
[13, 12, 9, 5, 1, 8, 7, 4, 0, 6, 2]
[13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2]

"""



"""
Question 2
"""




def mergeWithoutDuplicates(leftList, rightList):
    mergedList = []
    leftLen = len(leftList)
    rightLen = len(rightList)
    i = j = 0
    
    while(i < leftLen and j < rightLen):
        
        if (leftList[i] < rightList[j]):
            
            mergedList.append(leftList[i])
            
           
            i+=1
        
        elif (leftList[i] > rightList[j]):
            mergedList.append(rightList[j])
           
            j +=1
        
        
        elif (leftList[i] == rightList[j]):
            mergedList.append(rightList[j])
            i+=1
            j+=1

    while(i < leftLen):
        mergedList.append(leftList[i])
        
        i+=1
    
    while(j < rightLen):
        
         mergedList.append(rightList[j])
         
         j+=1
         
         
    return mergedList


def removeDuplicates(inpList):
    n = len(inpList)
    if (n <= 1):
        return inpList
    mid = int(n/2)
    leftList = removeDuplicates(inpList[0:mid])
    rightList =  removeDuplicates(inpList[mid:])
    return mergeWithoutDuplicates(leftList, rightList)


        
mylist = [1,2,3,4,6,4]

removeDuplicates(mylist)


"""
Question 7
"""
class linkedList():
    
    def __init__(self, value):
        
        self.value = value
        self.next = None
        pass
    def setNext(self,Obj):
        self.next = Obj
    def setValue(self,value):
        self.value = value
    def getNext(self):
        
        return self.next
    
    def getValue(self):
        return self.value
    
    
class hashTable():
    
    def __init__(self):
        self.HashTable = None
        self.size = None
    def createHashTable(self,size):
        self.HashTable = [None for i in range(size)]
        self.size = size
    
    def getHashVal(self,key):
        return key % self.size
    
    def insertToTable(self,key):
        indexInhash = self.getHashVal(key)
        
        if indexInhash < self.size:
            if self.HashTable[indexInhash] is None:
                
                self.HashTable[indexInhash] = linkedList(key) 
            
            else:
                nextLinkedList = self.HashTable[indexInhash]
                while True:
                        
                    if nextLinkedList.getNext() is None:
                        nextLinkedList.setNext(linkedList(key))
                        break
                    else:
       
                        nextLinkedList = nextLinkedList.getNext()
                        

    
    def checkKey(self,key):
        indexInhash = self.getHashVal(key)
        if indexInhash < self.size:
            
            if self.HashTable[indexInhash] is None:
                
                return False 
            
            else:
                nextLinkedList = self.HashTable[indexInhash]
                               
                while True:
                    value = nextLinkedList.getValue()
                    
                    if value == key:
                        return True
                        break
                    elif nextLinkedList.getNext() is None:
                        return False
                        break
                    
                    else:
       
                        nextLinkedList = nextLinkedList.getNext()
   

myHashTable = hashTable()
myHashTable.createHashTable(9)
for i in [5, 28, 19, 15, 20, 33, 12, 17, 10]:
    myHashTable.insertToTable(i)    
    
myHashTable.HashTable

myHashTable.checkKey(6)

for i in [5, 28, 19, 15, 20, 33, 12, 17, 10]:
    print(i%9)




"""
Question 10
"""
class binaryNode():
    
    def __init__(self,value = None):
        self._value = value
        self._left = None
        self._right = None
        self._parent = None
        
    def insert(self,insertValue):
        self._value = insertValue
     
    def getValue(self):
        return self._value 
        
    def getLeft(self):
        return self._left
    
    def setLeft(self,Node):
        self._left = Node
        
    def getRight(self):
        
        return self._right
    
    def setRight(self,Node):
        self._right = Node
        
        
class binaryTree():
    
    def __init__(self):
        self.root = None
        
        
    def insertInTree(self,insertValue):
        
        node = binaryNode(insertValue)
        if self.root is None:
            self.root = node
        
        else :
            currentNode = self.root    
            while True:
                
                if insertValue < currentNode.getValue():
                    if currentNode.getLeft() is None:
                        currentNode.setLeft(node)
                        break
                        
                    else:
                        currentNode = currentNode.getLeft()
                        
                    
                elif insertValue > currentNode.getValue():
                    
                    if currentNode.getRight() is None:
                        currentNode.setRight(node)
                        break
                    else:
                        currentNode = currentNode.getRight()
                        
    def walkInorder(self,currentNode):
        if currentNode is not None:
            self.walkInorder(currentNode.getLeft())
            print(currentNode.getValue())
            self.walkInorder(currentNode.getRight())
        
        
                  
          
          

myTree = binaryTree()
for i in range(10):
    myTree.insertInTree(i)
    
myTree.walkInorder(myTree.root)
    
    
    
"""
Question 5
"""

listOfBits = [0,0,0,0,0,0,0,0]
Index = 0
def incrementalCounter(listOfBits):
    global Index
    
    i = 0
    
    while i < len(listOfBits) and listOfBits[i] == 1:
        listOfBits[i] = 0
        i += 1
    if i < len(listOfBits):
        listOfBits[i] = 1
        Index = i    
    
def resetIndex(listOfBits):
    
    for j in range(Index+1):
        listOfBits[j] = 0
        
    pass

incrementalCounter(listOfBits)

resetIndex(listOfBits)
