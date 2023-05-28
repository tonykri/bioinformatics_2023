from read_data import read
from algorithm import create_matrix, play

brain_seq, muscle_seq = read()
print('Creating matrix...')
matrix = create_matrix(brain_seq, muscle_seq)
print('\nGame starts!')
play(matrix)
