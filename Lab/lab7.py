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



class binaryNode():
    
    def __init__(self,value = None):
        self._value = value
        self._left = None
        self._right = None
        self._parent = None
        self._height = 0
        
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
    
    
    
    
class binaryTree():
    
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
                        
                        break
                        
                    else:
                        currentNode = currentNode.getLeft()
                        
                    
                elif insertValue > currentNode.getValue():
                    
                    if currentNode.getRight() is None:
                        currentNode.setRight(node)
                        node.setParent(currentNode)
                        self.updateHeight(node.getParent())
                        
                        break
                    else:
                        currentNode = currentNode.getRight()
        
        
                        
    def walkInorder(self,currentNode):
        if currentNode is not None:
            self.walkInorder(currentNode.getLeft())
            print("Value : ",currentNode.getValue(),"height", currentNode.getHeight())
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
myTree = binaryTree()

#listOfNums = list(range(100))
for i in listOfNums:
    myTree.insertInTree(i)


print("Old tree order")
myTree.walkInorder(myTree.root)
#print(myTree.searchInTree(myTree.root,110))


B = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1000]
#B  = [37]
for element in B:
    returnNode = myTree.searchInTree(myTree.root,element)
    
    
#    print(returnNode)
    
    
    if (returnNode != False):
#        print("Heere")
        myTree.rotate(returnNode)


print("New tree order")
myTree.walkInorder(myTree.root)

