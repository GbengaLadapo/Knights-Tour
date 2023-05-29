import heapq
from copy import deepcopy
import time

# Define the initial state
initial_state = [
    ['B', ' ', 'B'],
    [' ', ' ', ' '],
    ['W', ' ', 'W']
]

# Define the goal state
goal_state = [
    ['W', ' ', 'W'],
    [' ', ' ', ' '],
    ['B', ' ', 'B']
]

# Define the knight moves
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def is_valid(x, y):
    """
    Check if a position is within the board.

    Parameters:
    x (int): The x-coordinate of the position.
    y (int): The y-coordinate of the position.

    Returns:
    bool: True if the position is within the board, False otherwise.
    """
    return 0 <= x < 3 and 0 <= y < 3

def get_knight_positions(state, knight):
    """
    Get the positions of the knights on the board.

    Parameters:
    state (list): The current state of the board.
    knight (str): The color of the knight ('W' for white, 'B' for black).

    Returns:
    list: A list of positions of the knights.
    """
    positions = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == knight:
                positions.append((i, j))
    return positions

def get_possible_moves(state, knight):
    """
    Get the possible moves for the knights.

    Parameters:
    state (list): The current state of the board.
    knight (str): The color of the knight ('W' for white, 'B' for black).

    Returns:
    list: A list of possible next states.
    """
    positions = get_knight_positions(state, knight)
    moves = []
    for pos in positions:
        x, y = pos
        for move in knight_moves:
            dx, dy = move
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and state[nx][ny] == ' ':
                new_state = deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                moves.append(new_state)
    return moves

def heuristic(state):
    """
    Heuristic function for A* search.

    Parameters:
    state (list): The current state of the board.

    Returns:
    int: The estimated cost to reach the goal from the current state.
    """
    wb = get_knight_positions(state, 'W')
    bb = get_knight_positions(state, 'B')
    gb_w = get_knight_positions(goal_state, 'W')
    gb_b = get_knight_positions(goal_state, 'B')
    h = 0
    for i in range(2):
        h += abs(wb[i][0] - gb_w[i][0]) + abs(wb[i][1] - gb_w[i][1])
        h += abs(bb[i][0] - gb_b[i][0]) + abs(bb[i][1] - gb_b[i][1])
    return h

def astar():
    """
    A* search algorithm.

    Returns:
    tuple: A tuple containing the minimum number of moves to reach the goal and the number of nodes expanded.
    """
    frontier = [(heuristic(initial_state), 0, initial_state)]
    explored = set()
    nodes_expanded = 0
    while frontier:
        f, g, state = heapq.heappop(frontier)
        if state == goal_state:
            return g, nodes_expanded
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple not in explored:
            explored.add(state_tuple)
            nodes_expanded += 1
            for knight in ['W', 'B']:
                next_states = get_possible_moves(state, knight)
                for next_state in next_states:
                    if tuple(tuple(row) for row in next_state) not in explored:
                        h = heuristic(next_state)
                        heapq.heappush(frontier, (g + h + 1, g + 1, next_state))

def branch_and_bound():
    """
    Branch and Bound search algorithm.

    Returns:
    tuple: A tuple containing the minimum number of moves to reach the goal and the number of nodes expanded.
    """
    frontier = [(0, initial_state)]
    explored = set()
    nodes_expanded = 0
    while frontier:
        g, state = heapq.heappop(frontier)
        if state == goal_state:
            return g, nodes_expanded
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple not in explored:
            explored.add(state_tuple)
            nodes_expanded += 1
            for knight in ['W', 'B']:
                next_states = get_possible_moves(state, knight)
                for next_state in next_states:
                    if tuple(tuple(row) for row in next_state) not in explored:
                        heapq.heappush(frontier, (g + 1, next_state))

# Measure and print the results
start = time.time()
g_astar, nodes_expanded_astar = astar()
end = time.time()
print("A* results:")
print("Minimum number of moves: ", g_astar)
print("Number of nodes expanded: ", nodes_expanded_astar)
print("Time taken: ", end - start)

start = time.time()
g_bb, nodes_expanded_bb = branch_and_bound()
end = time.time()
print("\nBranch and Bound results:")
print("Minimum number of moves: ", g_bb)
print("Number of nodes expanded: ", nodes_expanded_bb)
print("Time taken: ", end - start)
