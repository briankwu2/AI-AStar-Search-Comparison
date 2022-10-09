from inputOutput import *
from Node import *
from heapq import *


def recursiveDFS(node, goalStateList, count, maxDepth=10):
    if(node.depth == maxDepth + 1):
        return
    elif (node.evalState()):
        count[0] += 1
        node.setNumEnqueued(count[0])
        goalStateList.append(node)
        return
    count[0] += 1
    stateList = node.evalAction()
    for state in stateList:
        recursiveDFS(Node(state,node,node.depth+1), goalStateList, count, maxDepth) # Recursively goes through each child to evaluate goal state
        

def helperRecursiveDFS(node, goalStateList, count, maxDepth=10):
    recursiveDFS(node,goalStateList, count, maxDepth)
    if not goalStateList: # If the goalStateList is empty
        return False
    else:
        return True # Otherwise return true to signal that goal states were found

def printGoalPath(node):
    """
    Trace back until parent is None
    print the states
    """
    if node == None:
        return
    
    printGoalPath(node.parent) # Recursively
    displayState(node.state)
    print("\n")

def iterativeDeepeningSearch(root, goalStateList, count, maxDepth):
    """
    Performs IDS using the recursiveDFS function.
    Will change the max depth until
    """
    for iteration in range(1,maxDepth + 1):
        recursiveDFS(root, goalStateList, count, iteration)
    if not goalStateList: # If the goalStateList is empty
        return False
    else:
        return True # Otherwise return true to signal that goal states were found

def AStarAlgorithm(node, goalStateList, count, algType, prioQ, visitedList, maxDepth=10):
    """
    Pseudocode:
    First based on algType, use a different calcHeuristicX method
    if (node.depth == maxDepth + 1)
        return, don't use the function on the node
    Start from the root node
    use evalState
        if true then add node to goalList
        set the numEnqueued to the count of states
        return
    use evalActions() and store within a stateList
    for each state in stateList
        create a Node(state,the parent node, node.depth + 1)
        Call node.calcPathCost
        put the node into prioQ based on pathCost
    pop the first node in the prioQ and call AStarAlgorithm on it

    """


    if (node.depth == maxDepth + 1):
        return
    elif(node.evalState()):
        count[0] += 1
        node.setNumEnqueued(count[0])
        goalStateList.append(node)
        return
    count[0] += 1
    stateList = node.evalAction()
    for state in stateList:
        if state in visitedList:
            continue
        else:
            visitedList.append(state)
        childNode = Node(state, node, node.depth + 1)
        childNode.calcPathCost(algType)
        heappush(prioQ, childNode) # Pushes into prioQ based on pathCost
    AStarAlgorithm(heappop(prioQ),goalStateList,count,algType,prioQ,visitedList,maxDepth)


    


