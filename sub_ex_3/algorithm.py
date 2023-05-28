import numpy as np
import time

def create_matrix(brain_seq, liver_seq):
    N = len(brain_seq) + 1
    M = len(liver_seq) + 1

    matrix = np.empty([N, M], dtype=str)
    
    for i in range(1, N):
        matrix[i, 0] = 'F'
    for j in range(1, M):
        matrix[0, j] = 'F'

    for i in range(1, 3):
        for j in range(1, M):
            matrix[i, j] = 'W'
    for j in range(1, 3):
        for i in range(1, N):
            matrix[i, j] = 'W'

    matrix[0, 0], matrix[1, 1] = 'F', 'F'

    for i in range(3, N):
        for j in range(3, M):
            matrix[i, j] = 'L' if matrix[i-2, j-1] == 'W' and matrix[i-1, j-2] == 'W' else 'W'
    
    return matrix


def play(matrix):
    N, M = matrix.shape
    N, M = N-1, M-1
    finished = False
    player_1 = True

    print("\nPlayer 1 will lose...") if matrix[N, M] == 'L' else print("\nPlayer 2 will lose...")
    time.sleep(1)

    while finished is not True:
        if (N-2 < 0 or M-1 < 0) and (N-1 < 0 or M-2 < 0):
            finished = True
            break

        states = {
            'T' : '',
            'L' : ''
        }

        if (N-2 >= 0 and M-1 >= 0):
            if matrix[N-2, M-1] == 'F':
                finished = True
                break
            else:
                states['T'] = 'L' if matrix[N-2, M-1] == 'L' else 'W'
        
        if (N-1 >= 0 and M-2 >= 0):
            if matrix[N-1, M-2] == 'F':
                finished = True
                break
            else:
                states['L'] = 'L' if matrix[N-1, M-2] == 'L' else 'W'
        
        foundMove = False
        for state in states:
            if states[state] == 'L':
                foundMove = True
                if state == 'T':
                    N, M = N-2, M-1
                    break
                else:
                    N, M = N-1, M-2
                    break
        
        if not foundMove:
            for state in states:
                if states[state] == 'W':
                    if state == 'T':
                        N, M = N-2, M-1
                        break
                    else:
                        N, M = N-1, M-2
                        break

        player_1 = not player_1
    
    if player_1:
        print('\nPlayer 1 won!')
    else:
        print('\nPlayer 2 won!')
