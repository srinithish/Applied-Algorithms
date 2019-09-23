# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:25:54 2019

@author: nithish k
"""
filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab11_test_dijkstra.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >=0 :
#            print(line.strip("\n").split(sep = ' '))
            fromNode,toNode, weight,_ = line.strip("\n").split(sep = ' ')
            
            tupleToAdd = ((int(fromNode),int(toNode)),int(weight))
            listOfNums.append(tupleToAdd)
    file.close()
    return listOfNums      

          
listOfStrings = readFileToList(filePath)



class GraphNode():
    def __init__(self,graphNodeId):
        self.ID = graphNodeId
        self.visited = False
        self.distance = 0
        self.neighbours = []
        self.weights = []
        self.parent = None
        self.colour = 'White'
        self.startTime = 0
        self.endTime = 0
        self.set = None ## A or B
    def addNeighbour(self,graphNodeId):
        self.neighbours.append(graphNodeId)
    def getNeighbours(self):
        return self.neighbours
    def addWeight(self,weight):
        self.weights.append(weight)
        
        
def buildGraph(numNodes,listOfStrings):
    graphDict = {}
    for i in range(numNodes):
        graphDict[i] = GraphNode(i)
    for graphComb,weight in listOfStrings:
        graphDict[graphComb[0]].addNeighbour(graphComb[1])
        graphDict[graphComb[0]].addWeight(weight)
    return graphDict

graph = buildGraph(50,listOfStrings)

def initialiseSourceAndGraph(sourceID,graph):  

    for nodeID in graph:
        if nodeID == sourceID:
            graph[nodeID].distance = 0
        else:
            graph[nodeID].distance = float('inf')
    return graph

def relax(parentNode,childNode,weight):
    
    
    if childNode.distance > (parentNode.distance + weight):
       childNode.distance = parentNode.distance + weight
        
def dijkstra(sourceNodeID,graph):
    
    initialiseSourceAndGraph(sourceNodeID,graph) ## makes source 0 and allother distances as infinity

    prioityQueue = graph.copy() ### not a deep copy 
    
    while len(prioityQueue) > 0:
        
        ### extract min
        ## prirority queue implemented as array
        minDistNodeID = min(prioityQueue, key = lambda i:  prioityQueue[i].distance) 
        del prioityQueue[minDistNodeID]
    
        for childNodeID,weight in zip(graph[minDistNodeID].neighbours,graph[minDistNodeID].weights):
            
            parentNode = graph[minDistNodeID]
            childNode = graph[childNodeID]
            relax(parentNode,childNode,weight)
            

def getTargetDist(graph, sourceID, targetID):
    
    dijkstra(sourceID,graph)
    dist = graph[targetID].distance
    
    return dist


for i in range(11):
    print(getTargetDist(graph, 30, i))
    
