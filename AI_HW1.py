from inputOutput import *
from Node import *
import sys
from searchAlgorithms import *
MAX_DEPTH = 10 # if you want to change the max allowed depth

alg_name, state = interpretCLIArgs(sys.argv)

root = Node(state, None, 0)
goalList = []
prioQ = []
count = [0]
visitedList = []

if (alg_name == "dfs"):
    helperRecursiveDFS(root, goalList, count, MAX_DEPTH)
    
elif(alg_name == "ids"):
    iterativeDeepeningSearch(root, goalList,count, MAX_DEPTH)

elif(alg_name == "astar1"):
    AStarAlgorithm(root,goalList,count,"astar1",prioQ, visitedList, MAX_DEPTH)

elif(alg_name == "astar2"):
    AStarAlgorithm(root,goalList,count,"astar2",prioQ, visitedList, MAX_DEPTH)
else:
    print("Invalid type of algorithm")
    exit()

if len(goalList) == 0:
    print("Number of total states searched: " + str(count[0]))
    print("There was no solution within depth " + str(MAX_DEPTH))
    exit()

print("The " + alg_name + " Algorithm")
print("The num of states enqueued is: " + str(goalList[0].numEnqueued))
print("There are " + str(goalList[0].depth) + " moves")
print("This is the solution")

printGoalPath(goalList[0])


