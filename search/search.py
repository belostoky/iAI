# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


# def genericSearch(problem, fringe):
#
#     fringe.push((problem.getStartState(), None, 0))
#     explored = set()
#
#     while not fringe.isEmpty():
#         move = fringe.pop()
#         if move[0] in explored:
#             continue
#
#         if problem.isGoalState(move[0]):
#             return True, [move[1]]
#
#         explored.add(move[0])
#         successors = problem.getSuccessors(move[0])
#         for child in successors:
#             fringe.push(child)
#
#     return
#
#
#
#     if fringe.isEmpty():
#         return False, []
#
#     step = fringe.pop()
#     curr_state = step[0]
#
#     if problem.isGoalState(curr_state):
#         return True, [step[1]]
#
#     successors = problem.getSuccessors(curr_state)
#     for child in successors:
#         fringe.push(child)
#
#     for i in range(1, len(successors)):
#
#         result = genericSearch(problem, fringe)
#         if result[0]:
#             return True, result[1].insert(0, step[1])

def genericSearch(problem, fringe, visited):

    if fringe.isEmpty():
        return False, []

    moveTo = fringe.pop()

    if visited.__contains__(moveTo[0]):
        return False, []

    if problem.isGoalState(moveTo[0]):
        return True, [moveTo[1]]

    suc = problem.getSuccessors(moveTo[0])

    for child in suc:
            fringe.push(child)

    visited.add(moveTo[0])

    for i in range(0, len(suc)):
        result = genericSearch(problem, fringe, visited)
        if result[0]:
            result[1].insert(0, moveTo[1])
            return result

    return False, []




def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = util.Stack()
    start_state = problem.getStartState()
    fringe.push((start_state, None, 0))
    visited = set()
    result = genericSearch(problem, fringe, visited)
    return result[1][1:]    #returns everything but the first move 'None'

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch