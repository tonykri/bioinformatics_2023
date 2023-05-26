import numpy as np
import math
from probabilities import p_start, p_states, p_symbol

def get_scores(seq):
    score_grid = np.zeros((len(p_start),len(seq)))
    max_prev_prob = float('-inf')
    prev_state = None

    for col, symbol in enumerate(seq):
        if col == 0:
            for row, state in enumerate(p_states):
                score_grid[row, col] = math.log(p_start[state]) + math.log(p_symbol[state][symbol])
                if score_grid[row, col] > max_prev_prob:
                    max_prev_prob = score_grid[row, col]
                    prev_state = state
            continue
        for row, state in enumerate(p_states):
            score_grid[row, col] = max_prev_prob + math.log(p_states[state][prev_state]) + math.log(p_symbol[state][symbol])

    return score_grid

def get_path(score_grid, seq):
    path = []

    for col in reversed(range(len(seq))):
        symbol = seq[col]
        max = -1
        s = 0
        for row, state in enumerate(p_states):
            if score_grid[row, col] > max:
                max = score_grid[row, col]
                s = state
        path.append((s, symbol))

    path.reverse()
    return path
