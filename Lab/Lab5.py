# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:20:54 2019

@author: nithish k
"""

class linkedListNode():
    
    def __init__(self, value):
        
        self.value = value
        self.next = None
        self.previous = None
        
        pass
    
    def setNext(self,Obj):
        self.next = Obj
        
    def setValue(self,value):
        self.value = value
    
    
    def setPrevious(self,Obj):
        self.previous = Obj
        
    def getNext(self):
        
        return self.next
    
    def getPrevious(self):
        
        return self.previous
    def getValue(self):
        return self.value
    


class linkedList():
    
    def __init__(self):
        self.first = None
    
    def getFirst(self):
        return self.first.getValue()
    
    def getLast(self):
        if self.first is None:
            return self.first
        
        else:
            
            nextList = self.first.getNext()
            previousList = self.first
               
            while True:
                if nextList is None:
                    return previousList.getValue()
                    break
                else:
                    nextList  = nextList.getNext()

        
        
        
    def insertAsLast(self,value):
        insertList = linkedListNode(value)
        if self.first is None:
            
            self.first = insertList
            
        else:
            nextList = self.first.getNext()
            previousList = self.first
           
            while True:
                if nextList is None:
                    insertList.setPrevious(previousList)
                    previousList.setNext(insertList)
                    break
                else:
                    nextList  = nextList.getNext()
      
        
    def insertAtFirst(self,value):
        insertList = linkedListNode(value)
        if self.first is None:
            
            self.first = insertList
            
        else:
            self.first.setPrevious(insertList)
            insertList.setNext(self.first)
            self.first = insertList
        
    
myLinkedList = linkedList()

myLinkedList.insertAsLast(10)
myLinkedList.insertAtFirst(5)
myLinkedList.getFirst()



class binaryHeap():
    
    def __init__(self,initList = []):
        self.HeapList = initList
        self.size = len(initList)
    def _swap(self,pos1,pos2,listToBeAltered):
        temp = listToBeAltered[pos1]
        listToBeAltered[pos1] = listToBeAltered[pos2]
        listToBeAltered[pos2] = temp
   
    
    
    
    def siftdown(self,i):
        parent = self.heaparray[i]
        
        left_index = (i*2)+1
        right_index = (i*2)+2
        
        if right_index >= self.n and left_index >= self.n: # No childs nodes
            return False
        
        # There is no right child node to this node but there is left node
        elif right_index >= self.n and left_index < self.n:
            left_child = self.heaparray[left_index]
            if max(left_child,parent) == left_child: # Left child is greatest
                self.swapElements(left_index,i)
                self.siftdown(left_index)
        
        else: # There both nodes to this node
            right_child = self.heaparray[right_index]
            left_child = self.heaparray[left_index]
            
            if max(left_child,right_child,parent) == left_child: # Left child is greatest
                self.swapElements(left_index,i)
                self.siftdown(left_index)

            elif max(left_child,right_child,parent) == right_child: # right child is greatest
                self.swapElements(right_index,i)
                self.siftdown(right_index)

            else: # The parent is greater than the childs
                return True
            
            
    
    
    def siftDown(self,position):
        ##position form 1
        listToConvert = self.HeapList
        lastPossiblePosn = self.size -1
        initParent = listToConvert[position]
        newPosition = position
        
      
        
        if 2*position+1 > lastPossiblePosn and 2*position+2 > lastPossiblePosn : ##index in range or there exists a child
            return 
        
        
        
        elif 2*position+2 > lastPossiblePosn and 2*position+1 <= lastPossiblePosn: ### leftChild Exists
             ##pos
            leftChild = listToConvert[2*position+1] ##2*pos
            rightChild = -float("Inf")  ## 2*pos+1
            
    
        else:  ###both exists
            
            
            
            leftChild = listToConvert[2*position+1] ##2*pos
            rightChild = listToConvert[2*position+2]  ## 2*pos+1
                
            
    
        if  leftChild >= initParent and   leftChild >= rightChild: ##left child is the greatest
            self._swap(2*position+1,position,listToConvert) ##swap parent with right
            newPosition = 2*position+1
            
        
        elif  rightChild >= initParent and rightChild >= leftChild: ##right child is the greatest
            self._swap(2*position+2,position,listToConvert) ##swap parent with right
            newPosition = 2*position+2
        
        if newPosition != position:
#                print(listToConvert)
            
            self.siftDown(newPosition)
            

    def siftUp(self):
        
        pass

    def extractMax(self):
#        heapedList = self.HeapList
        maxElem = self.HeapList[0]
        self.HeapList[0] = self.HeapList[-1] 
        del self.HeapList[-1] 
        self.size -= 1
        if self.size != 0:
            self.siftDown(0)
            
        return maxElem

    def buildMaxHeap(self):
        listToConvert = self.HeapList
        ##from last but one layer of nodes do heapify
        lastPosition = len(listToConvert)-1
        
        for i in range(int((lastPosition-1)/2),-1,-1):

            self.siftDown(i)



filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab5_test_heap.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums


myList = readFileToList(filePath)
myHeap = binaryHeap(myList)
myHeap.buildMaxHeap()

for i in range(len(myList)):
    print(myHeap.extractMax())

