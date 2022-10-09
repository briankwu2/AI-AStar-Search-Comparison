from Node import *

def interpretCLIArgs(argv):
    """
    Interprets the command line arguments, and returns the option
    and initial state
    params: argv (system variable for CLI)
    returns algorithm choice, String List of state
    """
    alg_name = argv[1]
    input_file_path = argv[2]

    return alg_name, readInputFile(input_file_path)
    


def readInputFile(inputfile_path):
    """
    Takes in a file path, reads the first line and returns a list of substrings
    params: input file path
    returns: stringList
    """
    with open(inputfile_path) as file_object:
        string = file_object.readline().strip()
        stringList = string.rsplit(" ")
        print(stringList)
        return stringList

def displayState(stringList):
    """
    Takes in a stringList length of 9, and prints it in a 3x3 array
    params: stringList (of state)
    returns: true or false depending on if the list is length 9
    """
    if(len(stringList) != 9):
        return False
    else:
        for i in range(0,9,3):
            print(stringList[i] + " " + stringList[i+1] + " " + stringList[i+2])
    return True
