# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:29:58 2019

@author: bhagya
"""


class binaryHeap():
    
    def __init__(self,array):
        self.heaparray = array
        self.n = len(array)
        
    def buildHeap(self):
        # We start from the right-most index of the second-last layer/depth
        start_index = (self.n-1)//2
        
        # Keep doing the sift-down till you reach the node
        while start_index >= 0:
            self.siftdown(start_index)
            start_index -= 1
        return self
        
    def getHeap(self):
        return self.heaparray
     
        
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
     
    def delMax(self):
        max_element = self.heaparray[0]
        
        # As the root node will be removed, pick the last element from heap
        # and replace it with root then siftdown it restore the heap structure
        last_index = self.n - 1
        self.swapElements(last_index,0)
        
        # Remove the last element of this heap list and reduce size by 1
        self.heaparray.pop()
        self.n -= 1
        self.siftdown(0)
        
        return max_element
        
    
    def swapElements(self,i,j):
        temp = self.heaparray[i]
        self.heaparray[i] = self.heaparray[j]
        self.heaparray[j] = temp
        return True
data= open("C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab5_test_heap.txt",'r')
   
Array1 = data.readlines()
n =Array1[1]
Array1= Array1[2:]
Array1 = list(map(int, Array1))

heap = binaryHeap(Array1)
heap.buildHeap()

# print(heap.getHeap())

# Get the 20 max elements in this heap
for _ in range(20):
    print(heap.delMax())

