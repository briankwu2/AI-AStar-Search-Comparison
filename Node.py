from inputOutput import *
class Node():

    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.g = 0

    def __lt__(self,other): # compare function for heapq
        return self.pathCost < other.pathCost

    def setNumEnqueued(self, num):
        self.numEnqueued = num
    
    def calcHeuristic1(self):
        """
        Heuristic that evaluates to number of tiles in wrong position

        """
        heuristicCounter = 0
        placementDict = {
            0:'7',
            1:'8',
            2:'1',
            3:'6',
            4:'*',
            5:'2',
            6:'5',
            7:'4',
            8:'3'
        }
        for index, element in enumerate(self.state):
            if (element != placementDict[index]):
                heuristicCounter += 1
        return heuristicCounter
    
    def calcHeuristic2(self):
        """
        Calculates the Manhattan Distance between a tile and it's correct location
        """

        heuristicCounter = 0
        coordinatesDict = {
            0:(0,0),
            1:(0,1),
            2:(0,2),
            3:(1,0),
            4:(1,1),
            5:(1,2),
            6:(2,0),
            7:(2,1),
            8:(2,2)
        }

        placementDict = {
            '7':0,
            '8':1,
            '1':2,
            '6':3,
            '*':4,
            '2':5,
            '5':6,
            '4':7,
            '3':8
        }


        for index,element in enumerate(self.state):
            coord1 = coordinatesDict[index] # Gets the current tile's location
            coord2 = coordinatesDict[placementDict[element]] # Gets the the correct coordinate tile for the element
            heuristicCounter += abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
        return heuristicCounter


    def calcPathCost(self, algType):
        h = 0
        if (algType == "astar1"):
            self.g = self.parent.g + 1 # Calculates cost from start to this node
            h = self.calcHeuristic1()
        elif(algType == "astar2"):
            self.g = self.parent.g + 1
            h = self.calcHeuristic2()
        
        self.pathCost = self.g + h
        return self.pathCost

    def evalState(self):
        """
        Evaluates if the Node's state is the goal state.

        Returns true if state == goalState
        Returns false if state != goalState
        """
        goalState = ['7','8','1',
                     '6','*','2',
                     '5','4','3']

        if (goalState == self.state):
            return True
        else:
            return False

    def evalAction(self):
        """
        Evaluates what available actions are there to take based on the state.
        Returns a list of states.
        Assume the indexes of the state look like
        0 1 2
        3 4 5
        6 7 8

        """
        # Center Case --------------------------
        stateList = []
        if(self.state[4] == '*'): # If the empty tile is in the middle
            state1, state2, state3, state4 = self.state[:], self.state[:], self.state[:], self.state[:] # Make 4 copies of the state
            
            state1[4], state1[1] = state1[1], state1[4] # Swap the two values UP
            state2[4], state2[7] = state2[7], state2[4] # Swap the two values DOWN
            state3[4], state3[3] = state3[3], state3[4] # Swap the two values LEFT
            state4[4], state4[5] = state4[5], state4[4] # Swap the two values RIGHT
            
            stateList.append(state1)
            stateList.append(state2)
            stateList.append(state3)
            stateList.append(state4)
            return stateList

        # Middle-Side Cases ---------------------------------------
        elif(self.state[3] == "*"): # If empty left-middle
            stateList = []

            for i in range (0,3):
                stateList.append(self.state[:])
            stateList[0][3],stateList[0][0] = stateList[0][0], stateList[0][3] # Swap the value UP
            stateList[1][3],stateList[1][4] = stateList[1][4], stateList[1][3] # Swap the value RIGHT
            stateList[2][3],stateList[2][6] = stateList[2][6], stateList[2][3] # Swap the value DOWN

            return stateList
        elif(self.state[1] == "*"): # If empty top-middle 
            stateList = []

            for i in range (0,3):
                stateList.append(self.state[:])
            stateList[0][1],stateList[0][0] = stateList[0][0], stateList[0][1] # Swap the value LEFT
            stateList[1][1],stateList[1][4] = stateList[1][4], stateList[1][1] # Swap the value RIGHT
            stateList[2][1],stateList[2][2] = stateList[2][2], stateList[2][1] # Swap the value DOWN

            return stateList

        elif(self.state[7] == "*"): # If empty down-middle 
            stateList = []

            for i in range (0,3):
                stateList.append(self.state[:])
            stateList[0][7],stateList[0][8] = stateList[0][8], stateList[0][7] # Swap the value RIGHT 
            stateList[1][7],stateList[1][4] = stateList[1][4], stateList[1][7] # Swap the value UP
            stateList[2][7],stateList[2][6] = stateList[2][6], stateList[2][7] # Swap the value LEFT 

            return stateList

        elif(self.state[5] == "*"): # If empty right-middle 
            stateList = []

            for i in range (0,3):
                stateList.append(self.state[:])
            stateList[0][5],stateList[0][2] = stateList[0][2], stateList[0][5] # Swap the value UP
            stateList[1][5],stateList[1][4] = stateList[1][4], stateList[1][5] # Swap the value LEFT
            stateList[2][5],stateList[2][8] = stateList[2][8], stateList[2][5] # Swap the value DOWN

            return stateList
        # Corner Cases -----------------------------------------
        elif(self.state[0] == "*"): # Top-Left Corner
            stateList = []

            for i in range (0,2):
                stateList.append(self.state[:])

            stateList[0][0],stateList[0][3] = stateList[0][3], stateList[0][0] # Swap the value DOWN
            stateList[1][0],stateList[1][1] = stateList[1][1], stateList[1][0] # Swap the value RIGHT

            return stateList
        elif(self.state[2] == "*"): # Top-Right Corner
            stateList = []

            for i in range (0,2):
                stateList.append(self.state[:])
                
            stateList[0][2],stateList[0][1] = stateList[0][1], stateList[0][2] # Swap the value 
            stateList[1][2],stateList[1][5] = stateList[1][5], stateList[1][2] # Swap the value DOWN

            return stateList
        elif(self.state[8] == "*"): # Bottom-Right Corner
            stateList = []

            for i in range (0,2):
                stateList.append(self.state[:])

            stateList[0][8],stateList[0][5] = stateList[0][5], stateList[0][8] # Swap the value UP
            stateList[1][8],stateList[1][7] = stateList[1][7], stateList[1][8] # Swap the value LEFT

            return stateList
        elif(self.state[6] == "*"):
            stateList = []

            for i in range (0,2):
                stateList.append(self.state[:])

            stateList[0][6],stateList[0][3] = stateList[0][3], stateList[0][6] # Swap the value UP
            stateList[1][6],stateList[1][7] = stateList[1][7], stateList[1][6] # Swap the value RIGHT

            return stateList





       
    

"""
Current Objective:
Create Recursive search that finds the goal state and returns the goal state
Possible Directions:
- Record all the nodes that are a goal state by placing them into a passed in list
- Search all the possible nodes
- Once a goal state is found, add it to the goalList, and then return?

Next Objectives:
- Implement Iterative Deepening Search

- Implement A* Search, create a variable for function of heuristics
    - make a heuristic 1 and 2 that uses different measure of how good it is

"""
