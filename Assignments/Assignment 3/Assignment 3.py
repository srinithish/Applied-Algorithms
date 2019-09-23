# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:56:25 2019

@author: nithish k
"""


import random
###Question 1

probDictForWins = {}

def prob(AWinsTillNow,BWinsTillNow,NForMatchWin):
    probAWin = 0.5
    probBWin = 0.5
    if AWinsTillNow == NForMatchWin:
        return 1
    elif BWinsTillNow == NForMatchWin:
        return 0
    
    else:
        if (AWinsTillNow,BWinsTillNow) not in probDictForWins:
            probAWinsGameGivenAWinsNextMatch = probAWin*prob(AWinsTillNow+1,BWinsTillNow,NForMatchWin)
            probAWinsGameGivenBWinsNextMatch = probBWin*prob(AWinsTillNow,BWinsTillNow+1,NForMatchWin)
        
            probDictForWins[(AWinsTillNow,BWinsTillNow)] = probAWinsGameGivenAWinsNextMatch + probAWinsGameGivenBWinsNextMatch
            return probDictForWins[(AWinsTillNow,BWinsTillNow)]
        else:
            
            return probDictForWins[(AWinsTillNow,BWinsTillNow)]
    
prob(9,2,10)



### Question 2


allElems = [2,3,4,5,7,2]
subsetDict = {}
indexPath = []

def findSubset(index,totalSum,allElems):
    
    if totalSum > 0 and index < 0:
        return False
    
    elif totalSum == 0 and index >=0 : ## if rest of totalSum is zero 
        
        return True
    if totalSum < 0 :
        return False

    
    if allElems[index] <= totalSum: ##choose element at index and check
        if (index,totalSum) not in subsetDict:
            subsetDict[(index,totalSum)] = findSubset(index-1,
                                                      totalSum-allElems[index],
                                                      allElems)
            
            if subsetDict[(index,totalSum)] == True :
                indexPath.append(index)
        
            else:
                subsetDict[(index,totalSum)] = findSubset(index-1,totalSum,allElems)    
            
        
    
    else: ##element can be ruled out
        
        if (index,totalSum) not in subsetDict: 
            subsetDict[(index,totalSum)] = findSubset(index-1,totalSum,allElems)
        
    return subsetDict[(index,totalSum)]
        
            
findSubset(5,8,allElems)

    
    
###Question 3

##Dynamic programming bottom up




IsMaxMinInitialised = False
minList  = []
def maxDiffTillIndex(tillIndex,numList):
    
    global IsMaxMinInitialised
    global minList
    if not IsMaxMinInitialised:
        ##index from where min came, minValue
        
        minList = [[0,float("Inf")] for _ in numList]
#        maxList = [[0,-float("Inf")] for _ in numList]
        minList[0][1] = numList[0]
#        maxList[0][0] = numList[0]
        IsMaxMinInitialised = True
        
    ###prepare min list
    if numList[tillIndex] < minList [tillIndex-1][1]: ## next minimum is lesser
        minList [tillIndex][1] = numList[tillIndex] ##update minValue
        minList [tillIndex][0] = tillIndex ##update index from
        
        
    else : ## copy the previous minimums
        minList [tillIndex][1] = minList [tillIndex-1][1]
        minList [tillIndex][0] = minList [tillIndex-1][0]
    
#    ##prpare max list
#    if numList[tillIndex] > maxList [tillIndex-1]:
#        maxList[tillIndex] = numList[tillIndex]
#        
#    else :
#        maxList[tillIndex] = maxList[tillIndex-1]
    
    
    maxDiff = numList[tillIndex]-minList[tillIndex-1][1]
    
    
    
    
    return maxDiff, minList[tillIndex-1]




def getMaxDiff(numList):
    
    
    maxValue = -float("Inf")
    indexAt = 0
    
    
    for i in range(1,len(numList)):
        
        (maxDiff,(frmIndex,minValue))  = maxDiffTillIndex(i,numList)
    
        if maxDiff > maxValue:
            
            maxValue = maxDiff
            indexAt = frmIndex
            tillIndex = i
    return maxValue,indexAt,tillIndex
            
            
numList = [random.randint(0,100) for i in range(50000)]
getMaxDiff(numList)

        
        
###quesition 2 anohter version

allElems = [2,3,4,5,7,2]
subsetDict = {}
indexPath = []

def findSubset(index,totalSum,allElems):
    
    if index < 0 :
        return False
    
    elif index >=0 and totalSum == 0  : ## if rest of totalSum is zero 
        
        return True
    
    
    if totalSum < 0 :
        return False

    
  
        
    if (index,totalSum) not in subsetDict:
        subsetDict[(index,totalSum)] = findSubset(index-1,
                                                  totalSum-allElems[index],
                                                  allElems)
        
    if subsetDict[(index,totalSum)] == True :
        indexPath.append(index)

    else:
        subsetDict[(index,totalSum)] = findSubset(index-1,totalSum,allElems)    
            
        

        
    return subsetDict[(index,totalSum)]
    

findSubset(5,8,allElems)
    
    

###Question 4

def genRandomConnections(totalMembers):
##generate random connections
    listOfConnections = [(random.randint(0,totalMembers-1),
                          random.randint(0,totalMembers-1)) for _ in range(totalMembers*5)]
    
    ## get unique conncetions
    listOfConnections = list(set(listOfConnections))
    
    ## remove self connections
    listOfConnections = [conn for conn in listOfConnections if conn[0] != conn[1]]
    return listOfConnections

listOfConnections = genRandomConnections(30)


def convertToDictOfConnections(totalMembers,listOfConnections):
    
    dictOfConnections = {key:[] for key in range(totalMembers)}
    
    for frmNode,toNode in listOfConnections:
        if toNode not in dictOfConnections[frmNode]:
            dictOfConnections[frmNode].append(toNode)
        if frmNode not in dictOfConnections[toNode]:
            dictOfConnections[toNode].append(frmNode) 
    
    return dictOfConnections
    

dictOfConnections = convertToDictOfConnections(30,listOfConnections)


    
        

class graph():
    
    def __init__(self,dictOfNodesAndConnections = None):
        
        if dictOfNodesAndConnections is None:
            
        
            self.nodesAndEdges = {}
            
        else:
            self.nodesAndEdges = dict(dictOfNodesAndConnections)
        pass
    
    def addNode(self,node):
        if node not in self.nodesAndEdges:
            self.nodesAndEdges[node] = []
            
        pass
        
    
    def addEdge(self,frmNode,toNode):
        ## bi directional edges
        self.addNode(frmNode)
        self.addNode(toNode)
        
        if toNode not in self.nodesAndEdges[frmNode]:
            self.nodesAndEdges[frmNode].append(toNode)
        if frmNode not in self.nodesAndEdges[toNode]:
            self.nodesAndEdges[toNode].append(frmNode) 
        
        pass
    
    def getChildren(self,atNode):
        
        if atNode in self.nodesAndEdges:
            return self.nodesAndEdges[atNode]
        else:
            return []
    
    def delNode(self,node):
        if node in self.nodesAndEdges: 
            del self.nodesAndEdges[node]
        
        ## refresh connections
            
            for vertex in self.nodesAndEdges:
                if node in self.nodesAndEdges[vertex]:
                    self.nodesAndEdges[vertex].remove(node)
        else :
            pass
        
        

myOrigGraph = graph(dictOfConnections)
inviteGraph = graph(dictOfConnections)


def removeInvites(inviteGraph):
    
    while True:
    
        listOfNodes = list(inviteGraph.nodesAndEdges.keys())
        countOfRetainedInvites = 0
        for node in listOfNodes:
            
            ## known <5 or unknown < 5
            if len(inviteGraph.getChildren(node)) < 5 or  len(inviteGraph.nodesAndEdges) - len(inviteGraph.getChildren(node)) < 5 :
#                print(inviteGraph.nodesAndEdges)
#                print("Del :",node )
                inviteGraph.delNode(node)
                
                
            else:
                countOfRetainedInvites +=1
                
        if countOfRetainedInvites == len(listOfNodes):
            break;
    pass


removeInvites(inviteGraph)                 
inviteGraph.nodesAndEdges


##dynamic appraoch
NodeToInvite = {}
def retainInvites(node):
    
    if node in NodeToInvite :
        return NodeToInvite[node]
    
    
    if len(myOrigGraph.getChildren(node)) >= 5 and  len(myOrigGraph.nodesAndEdges) - len(myOrigGraph.getChildren(node)) >= 5 :
        
        listOfResults = []
        
        for child in myOrigGraph.getChildren(node):
            
            if child in NodeToInvite:
                listOfResults.append(NodeToInvite[child])
            else:
                listOfResults.append(retainInvites(child))
                
        if sum(listOfResults) >= 5 :
            NodeToInvite[node] = True
        else:
            NodeToInvite[node] = False
        
        return NodeToInvite[node]
                
        
        pass
            
            
            
for node in myOrigGraph.nodesAndEdges:
    retainInvites(node)
    
    
    
    
    
    
###Question 5
def isIntersecting(timeInt1, timeInt2):
    
    if timeInt1[0] > timeInt1[1] and timeInt2[0] > timeInt2[1] : 
    ## both crossing over night hence intersecting
        return True
    
    ##both proper spanning within

            
    ##one of it is over midnight
    ##if time1 is over midnight
    if timeInt1[0] > timeInt1[1] : #other time2 one is normal
        
        if timeInt1[0] >=  timeInt2[1] and timeInt1[1] <=  timeInt2[0] :
            return False
        else:
            return True
   
    ##if time2 is over midnight
    if timeInt2[0] > timeInt2[1] : #other one is normal
        
        if timeInt2[0] >=  timeInt1[1] and timeInt2[1] <=  timeInt1[0] :
            return False
        else:
            return True
    
    
    ## if both are normal
    if timeInt1[0] < timeInt1[1] and timeInt2[0] < timeInt2[1]:
    ##start1 between time2
        if timeInt1[0] >= timeInt2[0] and timeInt1[0] <= timeInt2[1]:
            return True
        ##start2 between time1
        if timeInt2[0] >= timeInt1[0] and timeInt2[0] <= timeInt1[1]:
            return True       
        
        else:
            return False
        
    else:
        
        return False
    
    
    
isIntersecting((7,4),(4,5))
jobNumbersPicked = []

def getIntersectionDict(listOfJobTimes):
    intersectionDict = {key: [] for key in listOfJobTimes}
    for i,jobI in enumerate( listOfJobTimes):
        
        for j,jobJ in enumerate( listOfJobTimes):
            
            if i != j and isIntersecting(jobI,jobJ):
                intersectionDict[jobI].append(jobJ)
                
            
    return intersectionDict

listOfJobTimes = [(18,6),(21,4),(3,14),(13,19)]



intersectionDict = getIntersectionDict(listOfJobTimes)

def removeIntersectionsOfJobChosen(jobChosen,listOfJobs):
    global intersectionDict
    if jobChosen in intersectionDict:
        for intJobs in intersectionDict[jobChosen]:
            if intJobs in listOfJobs: ##try except may be less expsensive
                listOfJobs.remove(intJobs)
        
    else:
        return False
        
    pass

def solveForMax(sortedList):
    
    
    while True:
        copySortedList = list(sortedList)
        if len(copySortedList) == 0:
            break;
        for job in copySortedList:
            ##pick a job remove its intersections if any
            removeIntersectionsOfJobChosen(job,sortedList) 
            
        ## there are no more elements removed or if there are no more intersections
        if len(sortedList) == len(copySortedList): 
            return sortedList        
            

def checkMidnightJobs(intersectionDict,listOfJobTimes):

    maxSolutionLen = -float("Inf")    
    for job in intersectionDict: 
        newListOfAllJobs = list(listOfJobTimes)
        if job[0] > job[1]:## choose a job that is over midnight    
            removeIntersectionsOfJobChosen(job,newListOfAllJobs)
            
            sortedJobs = sorted(newListOfAllJobs,key = lambda x: x[1])
            solution   = solveForMax(sortedJobs)
            if len(solution) > maxSolutionLen:
                maxSolutionLen = len(solution)
                maxSolution = solution
                
    return maxSolution   
            
checkMidnightJobs(intersectionDict,listOfJobTimes)

list(range(0,5))
[1,3][1:]
