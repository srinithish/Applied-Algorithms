# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:53:05 2019

@author: nithish k
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:01:24 2019

@author: nithish k
"""

import copy

import random

class binaryNode():
    
    def __init__(self,value = None):
        self._value = value
        self._left = None
        self._right = None
        self._parent = None
        self._height = 0
        self._priority  = random.random()  ##min value 
        
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
   
    def setParent(self,Node):
        self._parent = Node
        
    def getParent(self):
        return self._parent
     
    def setHeight(self,height):
        self._height = height

    def getHeight(self):
        return self._height
    
    def getPriority(self):
        return self._priority
    def setPriority(self,priority):
        self._priority = priority
    
    
class Treap():
    
    def __init__(self):
        self.root = None
        
        
    def insertInTree(self,insertValue):
        
        node = binaryNode(insertValue)
        node.setHeight(0)
        
        if self.root is None:
            self.root = node
        
        else :
            currentNode = self.root    
            while True:
                
                if insertValue <= currentNode.getValue():
                    if currentNode.getLeft() is None:
                        currentNode.setLeft(node)
                        node.setParent(currentNode)
                        self.updateHeight(node.getParent())
                        self.siftUp(node)
                        break
                        
                    else:
                        currentNode = currentNode.getLeft()
                        
                    
                elif insertValue > currentNode.getValue():
                    
                    if currentNode.getRight() is None:
                        currentNode.setRight(node)
                        node.setParent(currentNode)
                        self.updateHeight(node.getParent())
                        self.siftUp(node)
                        break
                    else:
                        currentNode = currentNode.getRight()
                        
        
                        
    def walkInorder(self,currentNode):
        if currentNode is not None:
            self.walkInorder(currentNode.getLeft())
            print("Value : ",currentNode.getValue(),
                  "height",currentNode.getHeight(),
                  "priority", currentNode.getPriority())
            self.walkInorder(currentNode.getRight())
        
    
    def searchInTree(self,currentNode,valueToSearch):
        
       
        if currentNode is None :
            return False
            
        elif currentNode.getValue() == valueToSearch :
            return currentNode
        
        elif valueToSearch <= currentNode.getValue():
            
            return self.searchInTree(currentNode.getLeft(),valueToSearch)
            
        elif valueToSearch > currentNode.getValue():
            
            return self.searchInTree(currentNode.getRight(),valueToSearch)
        
            
    
    def siftUp(self,atNode):
        
        
        if atNode is not None:
            
            
            while(atNode.getParent().getPriority() < atNode.getPriority()):
                
                self.rotate(atNode)
                if atNode is None or atNode.getParent() is None:
                    break;
                
        pass
    
    
    
    def rotateLeft(self, atNodeX):


#        x                                y
#       / \        rotate_right          / \
#      y   B         ---->              A   x
#     / \            <----                 / \
#    A   z         rotate_left            z   B
        
        
        
        yNode = atNodeX.getParent()
        zNode = atNodeX.getLeft()
        BNode = atNodeX.getRight()
        yParent = yNode.getParent()
        
        
        
        if yParent is None:
            self.root = atNodeX
        
        
        elif yParent.getLeft() == yNode: ##if y is leftChild
            yParent.setLeft(atNodeX)
        
        else :
            yParent.setRight(atNodeX) ## if y is right child
            
        ### at x
        atNodeX.setParent(yParent)
        atNodeX.setLeft(yNode)        
        
        ###on y
        yNode.setParent(atNodeX)
        yNode.setRight(zNode)
        
        
        ###on z
        
        if (zNode is not None ):
            zNode.setParent(yNode)
            
        self.updateHeight(atNodeX)    
        self.updateHeight(yNode)
        
        
        
        
        
        
        
        
        
        pass
    
    def rotateRight(self,atNodeX):
        
        
#        y                                x
#       / \        rotate_right          / \
#      x   B         ---->              A   y
#     / \            <----                 / \
#    A   z         rotate_left            z   B
        
        yNode = atNodeX.getParent()
        zNode = atNodeX.getRight()
        ANode = atNodeX.getLeft()
        yParent = yNode.getParent()
        
        if yParent is None:
            self.root = atNodeX
        
        
        elif yParent.getLeft() == yNode: ##if y is leftChild
            yParent.setLeft(atNodeX)
        
        else :
            yParent.setRight(atNodeX) ## if y is right child
            
        ### at x
        atNodeX.setParent(yParent)
        atNodeX.setRight(yNode)        
        
        ###on y
        yNode.setParent(atNodeX)
        yNode.setLeft(zNode)
        
        
        ###on z
        
        if (zNode is not None ):
            zNode.setParent(yNode)
            
            
        self.updateHeight(yNode)
        self.updateHeight(atNodeX)
        
        
        
        
        
        
        pass
    
    def rotate(self,atNode):
        
        
        if (atNode == self.root):
            return
        elif (atNode.getParent().getRight() == atNode):
            self.rotateLeft(atNode)
        else :
            self.rotateRight(atNode)
        
        
        
        pass
    
    def updateHeight(self,atNode):
        
        if atNode is None:
            return 
        
        oldHeight = atNode.getHeight()
        
        leftHeight = -1
        rightHeight = -1
        
        if atNode.getLeft() is not None:
            
        
            leftHeight = atNode.getLeft().getHeight()
            
        if atNode.getRight() is not None:
            
            rightHeight = atNode.getRight().getHeight()
        
        
        
        newHeight = 1+ max(leftHeight,rightHeight)
        
        if oldHeight == newHeight : ## if already updated 
            return 
        
        else :
            atNode.setHeight(newHeight)
            self.updateHeight(atNode.getParent()) ##update the heights of the paresnts as the child has
            ## the new height
            
        
        pass
    
                  
filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab7_test_RBST.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >=2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums      
          
listOfNums = readFileToList(filePath)

if __name__ == '__main__':
    myTreap = Treap()
    
    for i in range(5):
        for i in range(10**5):
            myTreap.insertInTree(i)
                
        print("Root data ,priority, height: ", myTreap.root.getValue(),myTreap.root.getPriority(),myTreap.root.getHeight())
        leftChild = myTreap.root.getLeft()
        rightChild = myTreap.root.getRight()
        print("Root's left child data, priority, height: ", leftChild.getValue(),leftChild.getPriority(),leftChild.getHeight())
        print("Root's right child data, priority, height: ",rightChild.getValue(),rightChild.getPriority(),rightChild.getHeight())
        
#    myTreap.walkInorder(myTreap.root)

