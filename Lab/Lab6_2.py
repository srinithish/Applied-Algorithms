# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:05:59 2019

@author: bhagya
"""

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)
                
def search(root,val):
    if root is None:
        return 0

    if root.data == val:
        return 1
        
    if (root.data > val):
        return search(root.l_child, val)
        
    if(root.data < val):
        return search(root.r_child, val)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

with open("lab6_test_BST.txt","r") as f:
    data=f.readlines()
x=[]
i=0
for line in data:
    if(i>0):
        x.append(int(''.join(line.split())))
    i=i+1
y=x[1:len(x)]
n=len(y)
r = Node(n)
for ele in y:
    binary_insert(r, Node(ele))
    
#search
z=0
for i in range(100):
    if(search(r,i) == 1):
        z=z+1
print(z)
in_order_print(r)