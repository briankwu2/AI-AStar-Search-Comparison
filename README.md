To run this code, run under python3
In the terminal use the format: python3 AI_HW1.py <algorithm_name> <input_file_path>

algorithm_name can take one of the following values:
- dfs : For running the Depth-first search algorithm
- ids : For running the Iterative deepening search algorithm
- astar1 : For running the A* algorithm with heuristic 1.
- astar2 : For running the A* algorithm with heuristic 2.
input_file_path : Path of the file containing the space separated input state.

For example - 6 7 1 8 2 * 5 4 3

The output will demonstrate the algorithm, num of enqueued states, and Depth
Then print out the path starting from initial state to goal state
in format of:
x x x
x * x
x x x 
where x are the numbers from {0...8} and * is the empty tile

Analysis:

When the program is run on the 3x3 array that looks like
6 7 1
8 2 *
5 4 3

The following number of enqueued states are as such for each algorithm:
dfs: 6056
ids: 6056
astar1: 8
astar2: 6

The Astar1 heuristic depends on the number of wrong tiles
The Astar2 heuristic depends on the manhattan distance from the correct tile

We see that the number of enqueued states vastly differ, and A* algos have the fastest search path by format
dfs and ids are similar but differ on other types of permutations
