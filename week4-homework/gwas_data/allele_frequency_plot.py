#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

allele_frequency = np.genfromtxt("plink.frq", dtype = float, encoding = None, skip_header = 1, usecols = (4))

fig, ax = plt.subplots()
ax.hist(allele_frequency, bins = 50)
ax.set_xlabel('Allele frequency')
ax.set_ylabel('Count')
ax.set_title('Distribution of Allele Frequencies')

plt.savefig('allele_frequency.png')