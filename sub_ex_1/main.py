from viterbi import get_scores, get_path

seq = 'GGCT'
score_grid = get_scores(seq)
path = get_path(score_grid, seq)

print('Score matrix:')
print(score_grid)

print('Most likely path:')
print(path)