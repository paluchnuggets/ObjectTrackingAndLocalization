# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    """
    Initialize 2d array of shape (nxn) and fill it with initial beliefs.
    Initial belief is calculated as an ratio (1.0 / number of all cells in a world)
    
    Parameters:
        grid - 2d array of shape (nxn) representing the world
    """
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    norm_val = 0
    for i, arr in enumerate(grid):
        row_belief = []
        for j, elem in enumerate(arr):
            if elem == color:
                new_elem = beliefs[i][j] * p_hit
            else:
                new_elem = beliefs[i][j] * p_miss
            row_belief.append(new_elem)
        norm_val += sum(row_belief)
        new_beliefs.append(row_belief)
    new_beliefs = [[(elem / norm_val) for elem in arr] for arr in new_beliefs ]
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)