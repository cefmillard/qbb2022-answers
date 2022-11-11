#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
import numpy.lib.recfunctions as rfn
from statsmodels.formula.api import ols
from statsmodels.regression.linear_model import RegressionResults

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names[1:])
row_names = list(input_arr['t_name'])
fpkm_values = np.array(input_arr[col_names[:]])
fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)

median = np.median(fpkm_values_2d, axis = 1)
fpkm_greater = fpkm_values_2d[np.where(median>0)]
fpkm_log2 = np.log2(fpkm_greater + 0.1)

linkage_row = linkage(fpkm_log2, 'ward')
linkage_column = linkage(fpkm_log2.T, 'ward')
leaves_row = leaves_list(linkage_row)
leaves_column = leaves_list(linkage_column)
row_sorted = fpkm_log2[leaves_row,:]
column_sorted = row_sorted[:,leaves_column]
fig, ax = plt.subplots()
ax.imshow(column_sorted, interpolation = 'nearest', aspect = 'auto')
plt.savefig('cluster_heatmap.png')
plt.close(fig)


fig = plt.figure(figsize=(25, 10))
dn = dendrogram(linkage_column)
plt.savefig('dendrogram_samples.png')

sexes=[]
stages=[]
for i in col_names:
    sexes.append(i.split('_')[0])
    stages.append(i.split('_')[1])

for i in range(fpkm_log2.shape[0]):
   list_of_tuples = []
   for j in range(len(col_names)):
     list_of_tuples.append((row_names[i],fpkm_log2[i,j], sexes[j], stages[j]))
longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
   
full_model = ols(formula = "fpkm ~ 1 + stage", data = longdf).fit()
print(full_model.summary())