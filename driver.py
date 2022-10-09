from inputOutput import *
from Node import *
import sys
from searchAlgorithms import *

node = Node(['6','7','1','8','2','*','5','4','3'], None, 0)

# stringList = readInputFile("hi.txt")
# displayState(stringList)

# print(node.state)
# print(node.depth)
# print(node.parent)

# # alg_name, stringList = interpretCLIArgs(sys.argv)
# stateList = node.evalAction()
# for state in stateList:
#     displayState(state)
#     print("\n")

# print(node.evalStateate())

goalList = []
count = [0]
prioQ = []
# print(helperRecursiveDFS(node, goalList, count))
# for goal in goalList:
#     print(str(goal.numEnqueued))
    
# print("The count is " + str(count[0]))
# print("The goal path is as defined: ")
# printGoalPath(goalList[0])
# iterativeDeepeningSearch(node, goalList, count)

# for goal in goalList:
#     print(str(goal.numEnqueued))
# print("There were " + str(len(goalList)) + " possible solutions")
# print("This is the first solution")
# printGoalPath(goalList[0])

# AStarAlgorithm(node,goalList,count,"astar1",prioQ)
# print("The AStar1 Algorithm")
# print("The num of states enqueued is: " + str(goalList[0].numEnqueued))
# print("There are " + str(goalList[0].depth) + " moves")
# print("This is the solution")
# printGoalPath(goalList[0])

# AStarAlgorithm(node,goalList,count,"astar2",prioQ)
# print("The AStar2 Algorithm")
# print("The num of states enqueued is: " + str(goalList[0].numEnqueued))
# print("There are " + str(goalList[0].depth) + " moves")
# print("This is the solution")
# printGoalPath(goalList[0])
"""
1 3 4
8 * 5
7 2 6
Expected Manhattan: 2 + 3 + 3 + 2 + 0 + 3 + 2 + 2 + 3 = 
Expected Wrong Tile #: 8
"""
node1 = Node(['1','3','4','8','*','5','7','2','6'], None, 0)
print(str(node1.calcHeuristic1()))
print(str(node1.calcHeuristic2()))
