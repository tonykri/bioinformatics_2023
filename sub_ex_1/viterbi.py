import numpy as np
import math
from probabilities import p_start, p_states, p_symbol

def get_scores(seq):
    score_grid = np.zeros((len(p_start),len(seq)))

    for col, symbol in enumerate(seq):
        if col == 0:
            for row, state in enumerate(p_states):
                score_grid[row, col] = math.log2(p_start[state]) + math.log2(p_symbol[state][symbol])
            continue

        for row, state in enumerate(p_states):
            score_grid[row, col] = math.log2(p_symbol[state][symbol]) + \
                  max(math.log2(p_states['a'][state]) + score_grid[0, col-1], math.log2(p_states['b'][state]) + score_grid[1, col-1])


    return score_grid

def get_path(score_grid, seq):
    path = []

    for col in reversed(range(len(seq))):
        max = float('-inf')
        selected_state = None

        for row, state in enumerate(p_states):
            if score_grid[row, col] > max:
                max = score_grid[row, col]
                selected_state = state

        path.append(selected_state)

    path.reverse()
    return path
