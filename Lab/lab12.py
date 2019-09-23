# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:28:10 2019

@author: nithish k
"""

def buildGraph(fileName,numNodes):
    parent = [nodeID for nodeID in range(numNodes)]
        
    # read from file and construct a graph
    f = open(fileName).readlines()
    
    edges = []
    for index,value in enumerate(f):
        node_list = value.strip().split(" ") # Second element is neighbor
        node = int(node_list[0])
        child = int(node_list[1])
        weight= int(node_list[2])
        edges.append((node, child, weight))
        # graph[node1].add_neighbour(node2)
    return parent, edges



def getAndSetParents(nodeID,parent):
    ##if the node amd the node match index then it is the root of the
    ## Tree, else get the parent of the node and reach its parent recursively and assign that to 
    ## the node now baiscally on the way make all of the childs parents equal
    
    ## say 1-2-3 1-4-6 make 2,3,4,6 all of the parents as the 1
    if parent[nodeID] != nodeID: 
        print("Indices :",list(range(9)))
        print("Pareny  :",parent)
        parent[nodeID] = getAndSetParents(parent[nodeID],parent)
    return parent[nodeID]


def makeUnion(nodeParent,nodeChild,parent):
    ## since biderrectional graph
    ## when you add it in the end you can imagine that the tail node is now the parent 
        

    parent[getAndSetParents(nodeChild,parent)] = nodeParent
    return parent



parent, edges = buildGraph("lab12_test_mst.txt",500)

edges = [(0,1,4),
         (1,2,8),
         (2,3,7),
         (3,4,9),
         (4,5,10),
         (5,6,2),(6,7,1),(7,0,8),(1,7,11),(7,8,7),(6,8,6),(8,2,2),(2,5,4),(5,3,14)]

parent  = list(range(9))

edges.sort(key=lambda x: x[2]) ##sort inplace according to weights


mstWeight = 0
for eTup in edges:
    node1 = eTup[0]
    node2 = eTup[1]
    weight = eTup[2]
    
    # if the two nodes do not belong to the same parent
    # then add this edge to the mst
    if getAndSetParents(node1,parent) != getAndSetParents(node2,parent):
        makeUnion(node1,node2,parent)
        mstWeight += weight
        

print(mstWeight)

