def read():
    f_brain = open("../data/brain_data/rna.fna", "r")
    f_liver = open("../data/liver_data/rna.fna", "r")

    brain_seq = f_brain.read()
    brain_seq = brain_seq.splitlines()
    idx = 1
    for sentence in brain_seq[1:]:
        if sentence.startswith(">"):
            break
        idx += 1
    brain_seq = ''.join(brain_seq[1:idx])

    liver_seq = f_liver.read()
    liver_seq = liver_seq.splitlines()
    idx = 1
    for sentence in liver_seq[1:]:
        if sentence.startswith(">"):
            break
        idx += 1
    liver_seq = ''.join(liver_seq[1:idx])

    return brain_seq, liver_seq
