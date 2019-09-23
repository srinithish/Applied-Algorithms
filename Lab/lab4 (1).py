# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:21:24 2019

@author: sidar
"""



import random


def swap(A, i, j): 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def quickSort(A, low, high):
    if low < high:
        index = random.randint(low,high-1)
        swap(A, low, index)

        p = partition(A, low, high)
        quickSort(A, low, p)
        quickSort(A, p+1, high)
    
def partition(A, low, high):
        i = low+1
        j = high-1
        pivot = A[low]
        while(i <= j) :
           
            while(i <= j and A[i] <= pivot ):
                i+=1
            while( j >=i and A[j] >= pivot ):
                j-=1
            if (i < j):
                swap(A, i, j)
                #i+=1
                #j-=1
        
        swap(A, low, j)
        return j

data= open("D:/Applied Algos/lab/lab4_test_sorting.txt",'r')
   
Array1 = data.readlines()
n =Array1[1]
Array1= Array1[2:]
Array1 = list(map(int, Array1))
print(Array1)
quickSort(Array1,0,len(Array1))        
print(Array1)

