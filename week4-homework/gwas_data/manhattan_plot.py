#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


CB1908_df = pd.read_csv('CB1908_IC50_gwas_results.assoc.linear', delim_whitespace = True)
GS451_df = pd.read_csv('GS451_IC50_gwas_results.assoc.linear', delim_whitespace = True)

CB1908_df = CB1908_df[CB1908_df['TEST'] == 'ADD']
GS451_df = GS451_df[GS451_df['TEST'] == 'ADD']

titles = ['CB1908 IC50 GWAS Results', 'GS451 IC50 GWAS Results']

for i, df in enumerate([CB1908_df, GS451_df]):
    df['minus_log10_pvalue'] = -np.log10(df.P)
    df.CHR = df.CHR.astype('category')
    df['index'] = range(len(df))
    df_grouped = df.groupby(('CHR'))
    df_sig = df[df['minus_log10_pvalue'] > 5]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['orange','green','blue', 'yellow']
    x_labels = []
    x_labels_pos = []
    
    for j, (name, group) in enumerate(df_grouped):
        group.plot(kind='scatter', x='index', y='minus_log10_pvalue',color=colors[j % len(colors)], ax=ax)
        x_labels.append(name)
        x_labels_pos.append((group['index'].iloc[0] + (group['index'].iloc[-1] - group['index'].iloc[0])/2))

    df_sig.plot(kind='scatter', x='index', y='minus_log10_pvalue', ax=ax, color = 'red')
    
    ax.set_title(titles[i])
    ax.set_xticks(x_labels_pos)
    ax.set_xticklabels(x_labels)
    ax.set_xlabel('Chromosome')
    plt.tight_layout()
    plt.savefig(titles[i]+ '.png')