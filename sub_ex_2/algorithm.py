import numpy as np
import random
import time

def create_matrix(brain_seq, muscle_seq):
    N = len(brain_seq) + 1
    M = len(muscle_seq) + 1

    matrix = np.empty([N, M], dtype=str)
    
    matrix[0,0] = 'F'
    for i in range(1, N):
        matrix[i, 0] = 'W'
    for j in range(1, M):
        matrix[0, j] = 'W'

    for i in range(1, N):
        for j in range(1, M):
            matrix[i, j] = 'W' if (i+j)%2==0 else 'L'
    
    return matrix


def play(matrix):
    N, M = matrix.shape
    N, M = N-1, M-1
    finished = False
    player_1 = True

    while finished is not True:
        move = random.randint(1, max(N, M))

        print('\nBrain sequence remaining symbols: %s' % N)
        print('Muscle sequence remaining symbols: %s' % M)
        print('Player 1 removes ', move, ' symbols') if player_1 else print('Player 2 removes ', move, ' symbols')
        time.sleep(.5)

        states = {
            'TL' : '',
            'L' : '',
            'T' : ''
        }

        if N-move >= 0 and M-move >= 0:
            if matrix[N-move, M-move] == 'F':
                finished = True
                break
            else:
                states['TL'] = 'L' if matrix[N-move, M-move] == 'L' else 'W'

        if N-move >= 0:
            if matrix[N-move, M] == 'F':
                finished = True
                break
            else:
                states['T'] = 'L' if matrix[N-move, M] == 'L' else 'W'
        
        if M-move >= 0:
            if matrix[N, M-move] == 'F':
                finished = True
                break
            else:
                states['L'] = 'L' if matrix[N, M-move] == 'L' else 'W'
        
        foundMove = False
        for state in states:
            if states[state] == 'L':
                foundMove = True
                if state == 'TL':
                    N, M = N-move, M-move
                    break
                elif state == 'T':
                    N = N-move
                    break
                else:
                    M = M-move
                    break
        
        if not foundMove:
            for state in states:
                if states[state] == 'W':
                    if state == 'TL':
                        N, M = N-move, M-move
                        break
                    elif state == 'T':
                        N = N-move
                        break
                    else:
                        M = M-move
                        break

        player_1 = not player_1
        
    
    if player_1:
        print('\nPlayer 1 won!')
    else:
        print('\nPlayer 2 won!')
