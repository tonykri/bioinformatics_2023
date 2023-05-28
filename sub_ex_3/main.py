from read_data import read
from algorithm import create_matrix, play
import time

brain_seq, liver_seq = read()
print('Creating matrix...')
matrix = create_matrix(brain_seq, liver_seq)
print('\nGame starts!')
time.sleep(1)
play(matrix)
