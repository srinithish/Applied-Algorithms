# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:45:50 2019

@author: nithish k
"""

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

listOfStrings = [((0,1),1),((1,2),2),((1,5),5),((2,4),4),((2,3),1),((4,5),3)]    
graph = buildGraph(6,listOfStrings)



"""
                        Question 1
"""
sortedNodes = []
currTime = 0
def DFSVisit(graphDict,currNodeID):
    global sortedNodes
    global currTime
    currTime +=1
#    print(currNodeID," start time ",currTime)
    graphDict[currNodeID].visited = True
    graphDict[currNodeID].startTime = currTime
    
    for neighNodeID in graphDict[currNodeID].neighbours:
        neigNode = graphDict[neighNodeID]
        
        if neigNode.visited == False:
#            print("Visiting ",neigNode.getID())
            neigNode.visited = True
            
            DFSVisit(graphDict,neighNodeID)
    
    
    currTime +=1
#    print(currNodeID," end time ",currTime)
    graphDict[currNodeID].endTime = currTime
    sortedNodes.append(currNodeID)
    
    
def DFS(graphDict):
    
    global currTime
    
    for nodeID,node in graphDict.items():
       
        if node.visited == False:
            
            
            DFSVisit(graphDict,node.ID)

def topologicalSort(graphDict):
    DFS(graphDict)
    return sortedNodes
  
  
topologicalSort(graph)


def checkExistantPath(sortedNodes,graphDict):
    
    for i in range(len(sortedNodes)-1):
        
        fromNode = sortedNodes[i]
        toNode = sortedNodes[i+1]
        ###may need to change this
        if toNode not in graphDict[fromNode].neighbours:
            return False
    
    return True
    
    
checkExistantPath(sortedNodes,graph)






"""
Question 3
"""

listOfConnections = [((0,1),1),((1,2),1),((0,3),1),((3,2),1)]
    
graph = buildGraph(5,listOfConnections)

def DFSCheck(graphDict,currNodeID):

    
    parentNode = graphDict[currNodeID]
    parentNode.visited = True
    
    for neighNodeID in parentNode.neighbours:
        neighNode = graphDict[neighNodeID]
        
        ## assign sets
        if neighNode.set is None:
            if parentNode.set == 'A':
                neighNode.set = 'B'
            elif parentNode.set == 'B':
                neighNode.set = 'A'
        
        ###  check compliance
        elif neighNode.set is not None:
            if parentNode.set == 'A' and neighNode.set == 'A':
                return False
            if parentNode.set == 'B' and neighNode.set == 'B':
                return False
                
        
        if neighNode.visited == False:

            neighNode.visited = True
            DFSCheck(graphDict,neighNodeID)
            
def isPartitioon(graphDict):
    
    
    for nodeID,node in graphDict.items():
       
        if node.visited == False:
            ## initialise with A
            node.set = 'A'
            
            
        Flag = DFSCheck(graphDict,node.ID)
            
    return False if Flag == False else True
    
print(isPartitioon(graph))
    


"""
Question 4
"""
import numpy as np
sortedNodes = []
currTime = 0
listOfConnections = [((0,1),1),((1,2),1),((0,3),1),((3,2),1)]
    
graph = buildGraph(4,listOfConnections)

sortedNodes = topologicalSort(graph)
sortedNodes = list(reversed(sortedNodes))


def assignSemesters(sortedNodes,graph):
    
    groupedCourses = [] ## list of lists
    semCourse = []
    prevNodeID = sortedNodes[0]
    semCourse.append(prevNodeID)
    
    for nextNodeID in sortedNodes[1:]:
        
        
        if nextNodeID not in graph[prevNodeID].neighbours: ## need to improve
            semCourse.append(nextNodeID)
            groupedCourses.append(semCourse)
            
        else:
            groupedCourses.append(semCourse)
            
            semCourse.append(nextNodeID)
            prevNodeID =  nextNodeID
    
    return groupedCourses


groupedCourses = assignSemesters(sortedNodes,graph)

def findLongestPaths(graph,source,weights):
    
    pass




import numpy as np
adjacencyMatrix = np.array([[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]])


def assignSemesters(adjacencyMatrix):
    
    listOfColumnNames = list(range(len(adjacencyMatrix[0]))) ### set of all columns
    
    listOfSems = []
    while (len(listOfColumnNames)>0):
        semCourses = []
        columnIndices = []
        for column in range(len(adjacencyMatrix)):
            if sum(adjacencyMatrix[:,column]) == 0: ## no incoming edges
                semCourses.append(listOfColumnNames[column])
                columnIndices.append(column)
        copyAdj = np.delete(adjacencyMatrix,semCourses,0) ### delete correspingin columns
        copyAdj = np.delete(copyAdj,semCourses,1) ## delete coreesonponding rows
        

        ## remove rest of the columns
        
        listOfColumnNames = np.delete(listOfColumnNames, columnIndices)
            
        
        adjacencyMatrix = copyAdj
        
        listOfSems.append(semCourses)
        
        

        
    return listOfSems

listOfSems = assignSemesters(adjacencyMatrix)
    


##### Question 6

import numpy as np

listOfConnections = [((0,1),2),((1,2),1),((0,3),1),((3,2),1),((2,0),2),((4,5),1)]

graph = buildGraph(6,listOfConnections)

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
    
    initialiseSourceAndGraph(sourceNodeID,graph)
    ### extract min
    prioityQueue = graph.copy() ### not a deep copy 
    
    while len(prioityQueue) > 0:
        
        ### extract min
        ##best implemented as prirority queue
        minDistNodeID = min(prioityQueue, key = lambda i:  prioityQueue[i].distance) 
        del prioityQueue[minDistNodeID]
    
        for childNodeID,weight in zip(graph[minDistNodeID].neighbours,graph[minDistNodeID].weights):
            
            parentNode = graph[minDistNodeID]
            childNode = graph[childNodeID]
            relax(parentNode,childNode,weight)
            

    


def findShortestCycle(graph):
    cycleLenghts = []
    for startVertex in graph:
        dijkstra(startVertex,graph)
        
        for endVertex in graph:
            weight = float('inf')
            if startVertex in graph[endVertex].neighbours:
                weightIndex = graph[endVertex].neighbours.index(startVertex)
                weight =  graph[endVertex].weights[weightIndex]
            cycleLength = weight + graph[endVertex].distance
            cycleLenghts.append(cycleLength)

    shortest = min(cycleLenghts)
    if shortest == float('inf'):
        return 'No Cycle'
    else:
        return shortest
    
findShortestCycle(graph)