# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:24:40 2019

@author: nithish k
"""




class GraphNode():
    
    
    def __init__(self,graphNodeId):
        self.graphNodeId = graphNodeId
        self.visited = False
        self.distance = 0
        self.neighbours = []
        
    def addNeighbour(self,graphNodeId):
        self.neighbours.append(graphNodeId)
        
    def getNeighbours(self):
        
        return self.neighbours





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


def buildGraph(numNodes = 50):
    graphDict = {}
    for i in range(numNodes):
        graphDict[i] = GraphNode(i)
        
    for graphComb in listOfStrings:
        
        graphDict[graphComb[0]].addNeighbour(graphComb[1])
        
    return graphDict
    
    
graph = buildGraph(50)
graph[4].getNeighbours()

#graph[10].get
def BFSSearch(graphDict,sourceID,destinationID):
    
    if sourceID == destinationID:
        return 0
    
    
    ### resset visited states
    
    graphDict[sourceID].visited = True
    graphDict[sourceID].distance = 0
    
    listAsQueue = []
    listAsQueue.append(sourceID)
    
    while(len(listAsQueue) > 0):
#        print("here")
        
        nodeIDtoExplore = listAsQueue.pop(0)
        
        curDistance  = graphDict[nodeIDtoExplore].distance
        
        for neighID in graphDict[nodeIDtoExplore].getNeighbours():
            
            neigh = graphDict[neighID]
#            print(neigh.distance)
            if destinationID == neigh.graphNodeId:
                return curDistance + 1
            
            if neigh.visited == False:
                neigh.visited = True
                graphDict[neighID].distance = curDistance + 1
                
#                print(graphDict[neighID].distance)
                
                listAsQueue.append(neighID)




    return False
            
                
            
print(BFSSearch(graph, 39, 4))
        

    
    


       
        