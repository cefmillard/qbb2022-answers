#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
from fasta import readFASTA

fasta_file = sys.argv[1]
scoring_matrix = np.genfromtxt(sys.argv[2], dtype = int, encoding = None, names = True)
gap_penalty = int(sys.argv[3])
output_file = sys.argv[4]

if scoring_matrix.shape == (23,):
    scoring_df = pd.DataFrame(scoring_matrix, index = ('A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X'))
else:
    scoring_df = pd.DataFrame(scoring_matrix, index = ('A', 'C', 'G', 'T'))

input_sequences = readFASTA(open(fasta_file))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]


F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), dtype = int)
trace_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1), dtype = str)

for i in range(len(sequence1)+1):
    F_matrix[i, 0] = i * gap_penalty
    trace_matrix[i][0] = "U"

for j in range(len(sequence2)+1):
    F_matrix[0, j] = j * gap_penalty
    trace_matrix[0][j] = "L"
    
F_matrix[0][0] = 0
trace_matrix[0][0] = "N"

for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        if sequence1[i-1] == sequence2[j-1]:
            d = F_matrix[i-1, j-1] + scoring_df[sequence1[i-1]][sequence2[j-1]]
        else:
            d = F_matrix[i-1, j-1] + scoring_df[sequence1[i-1]][sequence2[j-1]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)

        if (d >= h):
                        if (d >= v):
                            trace_matrix[i][j] = "D"
                        else:
                            trace_matrix[i][j] = "L"
        else:
                        if (h >= v):
                            trace_matrix[i][j] = "U"
                        else:
                            trace_matrix[i][j] = "L"


align1 = ""
align2 = ""
tracking = ""
i = len(sequence1)
j = len(sequence2)

tracking_score = []
while i > 0 or j > 0:
        tracking = tracking + trace_matrix[i][j]
        tracking_score.append(F_matrix[i][j])
        if (trace_matrix[i][j] == "D"):
            align1 = align1 + sequence1[i-1:i]
            align2 = align2 + sequence2[j-1:j]
            i=i-1
            j=j-1
        elif (trace_matrix[i][j] == "L"):
            align1 = align1 + sequence1[i-1:i]
            align2 = align2 + "-"
            i=i-1
        elif (trace_matrix[i][j] == "U"):
            align1 = align1 + "-"
            align2 = align2 + sequence2[j-1:j]
            j=j-1
align1 = align1[::-1]
align2 = align2[::-1]
tracking = tracking[::-1]

f = open(output_file, "a")
f.write(f'Sequence 1: {align1} \n')
f.write(f'Sequence 2: {align2} \n')
f.close()

print ("sequence 1 gaps:", align1.count('-'))
print ("sequence 2 gaps:", align2.count('-'))
print (" score:", F_matrix[len(sequence1)][len(sequence2)], file=sys.stderr)
