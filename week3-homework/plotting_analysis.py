#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
from vcfParser import parse_vcf

fname = sys.argv[1]
vcf = parse_vcf(fname)

depth = []
genotype_quality = []
allele_frequency = []
predicted_effect = []

for i in range(1, len(vcf)):
    variant = vcf[i]
    allele_frequency.append(variant[7]["AF"])
    annotations = variant[7]["ANN"].split(',')
    annotations = [item.split('|') for item in annotations]
    for item in annotations:
        predicted_effect.append(item[1])
    for j, ID in enumerate(variant[8]):
        if ID =='GQ':
            for k in range(9, len(variant)):
                genotype_quality.append(variant[k][j])
        elif ID == 'DP':
            for k in range(9, len(variant)):
                depth.append(variant[k][j])
        else:
            continue

predicted_effect = [item.split('&') for item in predicted_effect]
predicted_effect = [eff for item in predicted_effect for eff in item]
predicted_effect = [eff for eff in predicted_effect if eff]
effect_names, counts = np.unique(np.array(predicted_effect), return_counts = True)

genotype_organized = []
for i in genotype_quality:
    try:
        gq = float(i)
        genotype_organized.append(gq)
    except:
        continue

depth_organized = []
for i in depth:
    try:
        dp = int(i)
        depth_organized.append(dp)
    except:
        continue

fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize = (12,10))

ax[0,0].hist(depth_organized, color = 'red')
bins = np.arange(0, max(depth_organized) + 20, 20)
ax[0,0].set_yscale('log')
ax[0,0].set_xlabel('Read Depth')
ax[0,0].set_ylabel('Variant Frequency')

ax[0,1].hist(genotype_organized, bins = 16, color = 'blue')
ax[0,1].set_xlabel('Genotype Quality')
ax[0,1].set_ylabel('Variant Frequency')

ax[1,0].hist(genotype_organized, bins = 10, color = 'orange')
ax[1,0].set_xlabel('Allele Frequency')
ax[1,0].set_ylabel('Variant Frequency')

plt.xticks(rotation=45, ha='right')
ax[1,1].bar(effect_names, counts)
ax[1,1].set_yscale('log')
ax[1,1].set_xlabel('Predicted Effects')
ax[1,1].set_ylabel('Variant Frequency')

plt.tight_layout()

plt.savefig('analysis_plot.png')