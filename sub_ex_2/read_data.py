def read():
    f_brain = open("../data/brain_data/rna.fna", "r")
    f_muscle = open("../data/muscle_data/rna.fna", "r")

    brain_seq = f_brain.read()
    brain_seq = brain_seq.splitlines()
    idx = 1
    for sentence in brain_seq[1:]:
        if sentence.startswith(">"):
            break
        idx += 1
    brain_seq = ''.join(brain_seq[1:idx])

    muscle_seq = f_muscle.read()
    muscle_seq = muscle_seq.splitlines()
    idx = 1
    for sentence in muscle_seq[1:]:
        if sentence.startswith(">"):
            break
        idx += 1
    muscle_seq = ''.join(muscle_seq[1:idx])

    return brain_seq, muscle_seq