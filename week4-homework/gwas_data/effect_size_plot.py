#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vcfParser import parse_vcf
import seaborn as sb

GS451_df = pd.read_csv('GS451_IC50_gwas_results.assoc.linear', delim_whitespace = True)
GS451_df = GS451_df[GS451_df['TEST'] == 'ADD']

GS451_top_snp = GS451_df.loc[GS451_df['P'] == GS451_df['P'].min(),'SNP'].item()

CB1908_df = pd.read_csv('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
CB1908_df = CB1908_df[CB1908_df['TEST'] == 'ADD']

CB1908_top_snp = CB1908_df.loc[CB1908_df['P'] == CB1908_df['P'].min(),'SNP'].item()

genotypes = pd.DataFrame(parse_vcf('genotypes.vcf'))

genotype_list = genotypes[genotypes[2] == GS451_top_snp].values.tolist()[0][9:]

phenotype = pd.read_csv('GS451_IC50.txt', delim_whitespace = True)

phenotype_list = phenotype['GS451_IC50']

homo_ref = []

het = []

homo_alt = []

for i, gen in enumerate(genotype_list):
    if gen == '0/0':
        homo_ref.append(phenotype_list[i])
    elif gen == '0/1' or gen == '1/0':
        het.append(phenotype_list[i])
    elif gen == '1/1':
        homo_alt.append(phenotype_list[i])
    else:
        continue

fig, ax = plt.subplots()

ax = sb.boxplot(data = [homo_ref, het, homo_alt])
ax.set_xticklabels(['Homozygous Reference', 'Heterozygous', 'Homozygous Alternate'])
ax.set_ylabel('IC50')
plt.title('Effect size of ' + GS451_top_snp + ' on GS451 IC50')

plt.savefig('effect_size_plot.png')

print(GS451_top_snp)
print(CB1908_top_snp)