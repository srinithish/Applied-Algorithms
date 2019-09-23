# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:01:24 2019

@author: nithish k
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
                
                if insertValue <= currentNode.getValue():
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
        
        
                  
filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab6_test_BST.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >2 :
            listOfNums.append(int(line.strip("\n")))
    
    file.close()
    return listOfNums      
          
listOfNums = readFileToList(filePath)
myTree = binaryTree()


for i in listOfNums:
    myTree.insertInTree(i)
    
myTree.walkInorder(myTree.root)