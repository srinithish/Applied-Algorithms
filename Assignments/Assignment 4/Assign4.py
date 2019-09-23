# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:25:44 2019

@author: nithish k
"""

class GraphNode():
    
    
    def __init__(self,graphNodeId):
        self._graphNodeId = graphNodeId
        self._visited = False
        self._distance = 0
        self._neighbours = []
        self._parent = None
        self._colour = 'White'    
        self.startTime = 0
        self.endTime = 0
    def getID(self):
        return self._graphNodeId
    def setParent(self,ParentNode):
        self._parent = None
    
    def getParent(self):
        return self._parent
        
    def getDistance(self):
        return self._distance
    
    def setDistance(self,dist):
        self._distance = dist
    
    def getColour(self):
        return self._colour
    
    def setColour(self,color):
        self._colour = color
        
    def setVisited(self,Flag = True):
        self._visited = Flag
    
    def isVisited(self):
        return self._visited
    
    def addNeighbour(self,graphNodeId):
        self._neighbours.append(graphNodeId)
        
    def getNeighbours(self):
        
        return self._neighbours
    
 
    
    

filePath = "C:/Users/ntihish/Documents/IUB/Applied Algos/Lab/lab10_test_bfs.txt"
def readFileToList(filePath):
    file = open(filePath,"r") 
    listOfNums = []
    for lineNum,line in enumerate(file):
        
        if lineNum >=0 :
            
            fromNode,toNode = line.strip("\n").split(sep = ' ')
            listOfNums.append((int(fromNode),int(toNode)))
    file.close()
    return listOfNums      

          
listOfStrings = readFileToList(filePath)

listOfStrings = [(0,1),(1,2),(1,5),(2,4),(2,3),(4,5)]
def buildGraph(numNodes):
    graphDict = {}
    for i in range(numNodes):
        graphDict[i] = GraphNode(i)
        
    for graphComb in listOfStrings:
        
        graphDict[graphComb[0]].addNeighbour(graphComb[1])
        
    return graphDict

    
graph = buildGraph(6)

###graph dict of nodes and neighobours as list of NodeIDs

currTime = 0

#def DFSVisit(graphDict,currNodeID):
#    global currTime
#    currTime +=1
##    print(currNodeID," start time ",currTime)
#    graphDict[currNodeID].setVisited(True)
#    graphDict[currNodeID].startTime = currTime
#    
#    for neighNodeID in graphDict[currNodeID].getNeighbours():
#        neigNode = graphDict[neighNodeID]
#        
#        if neigNode.isVisited() == False:
##            print("Visiting ",neigNode.getID())
#            neigNode.setVisited(True)
#            
#            DFSVisit(graphDict,neighNodeID)
#    
#    
#    currTime +=1
##    print(currNodeID," end time ",currTime)
#    graphDict[currNodeID].endTime = currTime
#    
#    
#        
#    
#
#def DFS(graphDict):
#    
#    global currTime
#    
#    for nodeID,node in graphDict.items():
#       
#        if node.isVisited() == False:
#            
#            
#            DFSVisit(graphDict,node.getID())
#            
#            
#    
#DFS(graph)

#### Question 1 ################################################################

sortedNodes = []
currTime = 0
def DFSVisit(graphDict,currNodeID):
    global sortedNodes
    global currTime
    currTime +=1
#    print(currNodeID," start time ",currTime)
    graphDict[currNodeID].setVisited(True)
    graphDict[currNodeID].startTime = currTime
    
    for neighNodeID in graphDict[currNodeID].getNeighbours():
        neigNode = graphDict[neighNodeID]
        
        if neigNode.isVisited() == False:
#            print("Visiting ",neigNode.getID())
            neigNode.setVisited(True)
            
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

### topological sort of the graph    
topologicalSort(graph)
sortedNodes

def checkExistantPath(sortedNodes,graphDict):
    
    for i in range(len(sortedNodes)-1):
        
        fromNode = sortedNodes[i]
        toNode = sortedNodes[i+1]
        ###may need to change this
        if toNode not in graphDict[fromNode].getNeighbours():
            return False
    
    return True
    
    
checkExistantPath(sortedNodes,graph)
        
##### Question 2 #############################################################


#############################################################################


#####################Question 3##########################################




class GraphNode():
    
    def __init__(self,graphNodeId):
        self.ID = graphNodeId
        self.visited = False
        self.distance = 0
        self.neighbours = []
        self.parent = None  
        self.set = None ## A or B
        
    def addNeighbour(self,graphNodeId):
        self.neighbours.append(graphNodeId)

listOfStrings = [(0,1),(1,2),(2,3),(3,0),(2,4)]
    
graph = buildGraph(5)
    


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
            
        
                
            
            
    


def isParition(graphDict):
    
    
    for nodeID,node in graphDict.items():
       
        if node.visited == False:
            ## initialise with A
            node.set = 'A'
            
            
        Flag = DFSCheck(graphDict,node.ID)
            
    return False if Flag == False else True
    
print(parition(graph))
    
    
    

#### Question 4

listOfStrings = [(0,1),(1,2),(0,3),(3,2)]
    
graph = buildGraph(5)
    

sortedNodes = topologicalSort(graph)
























