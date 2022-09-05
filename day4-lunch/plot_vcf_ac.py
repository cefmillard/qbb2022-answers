#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

ac = np.array(ac)
ac = np.log10(ac+1)

title=vcf.split(".")[0]

fig, ax = plt.subplots()
ax.hist( ac, density=True )
#ax.set_yscale('log', base=10)
ax.set_ylim([0, 1])
ax.set_xlabel("Allele Count")
ax.set_ylabel("Frequency")
ax.set_title(f"Frequency of Allele Counts for {title}")
fig.savefig( vcf + ".png" )

fs.close()

