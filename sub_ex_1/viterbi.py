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

        temp_max_prev_prob = float('-inf')
        temp_prev_state = None

        for row, state in enumerate(p_states):
            score_grid[row, col] = max_prev_prob + math.log(p_states[state][prev_state]) + math.log(p_symbol[state][symbol])
            if score_grid[row, col] > temp_max_prev_prob:
                    temp_max_prev_prob = score_grid[row, col]
                    temp_prev_state = state

        max_prev_prob = temp_max_prev_prob
        prev_state = temp_prev_state

    return score_grid

def get_path(score_grid, seq):
    path = []

    for col in reversed(range(len(seq))):
        symbol = seq[col]
        max = float('-inf')
        selected_state = None

        for row, state in enumerate(p_states):
            if score_grid[row, col] > max:
                max = score_grid[row, col]
                selected_state = state

        path.append(selected_state)

    path.reverse()
    return path
