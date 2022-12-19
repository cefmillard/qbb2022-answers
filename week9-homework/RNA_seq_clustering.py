#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
import numpy.lib.recfunctions as rfn
from statsmodels.formula.api import ols
from statsmodels.regression.linear_model import RegressionResults
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.multitest import multipletests 

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
plt.close(fig)

sexes=[]
stages=[]
for i in col_names:
    sexes.append(i.split('_')[0])
    stages.append(i.split('_')[1])

p_values = []
beta_coefficients = []

for i in range(fpkm_log2.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)):
       list_of_tuples.append((row_names[i],fpkm_log2[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    full_model = ols(formula = "fpkm ~ stage", data = longdf).fit()
    p_values.append(full_model.pvalues['stage'])
    beta_coefficients.append(full_model.params['stage'])

pvalues_array = np.array(p_values)

sm.qqplot(pvalues_array, dist = stats.uniform, line = '45')
plt.savefig('qqplot.png')
plt.close()

fdr = np.array(multipletests(pvalues_array, alpha = 0.1, method = 'fdr_bh')[0])
differential_index = []
differential_index = np.where(fdr)[0]

differential_transcripts = []

for i in differential_index:
    differential_transcripts.append(row_names[i])

np.savetxt('differential_transcripts.txt', differential_transcripts, fmt='%s')

sex_controlled_p_values = []
sex_controlled_beta_coefficients = []

for i in range(fpkm_log2.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)):
       list_of_tuples.append((row_names[i],fpkm_log2[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    sex_controlled_full_model = ols(formula = "fpkm ~ stage + sex", data = longdf).fit()
    sex_controlled_p_values.append(sex_controlled_full_model.pvalues['stage'])
    sex_controlled_beta_coefficients.append(sex_controlled_full_model.params['stage'])

sex_controlled_pvalues_array = np.array(sex_controlled_p_values)
sex_controlled_beta_coefficients_array = np.array(sex_controlled_beta_coefficients)

sex_controlled_fdr = multipletests(sex_controlled_pvalues_array, alpha = 0.1, method = 'fdr_bh')[0]

sex_controlled_differential_index = []
sex_controlled_differential_index = np.where(sex_controlled_fdr)[0]

sex_controlled_differential_transcripts = []
sex_controlled_significant_b_coef = []
sex_controlled_significant_p_values = []

for i in sex_controlled_differential_index:
    sex_controlled_differential_transcripts.append(row_names[i])
    sex_controlled_significant_b_coef.append(sex_controlled_beta_coefficients_array[i])
    sex_controlled_significant_p_values.append(sex_controlled_pvalues_array[i])

np.savetxt('sex_controlled_differential_transcripts.txt', sex_controlled_differential_transcripts, fmt='%s')

sex_controlled_significant_p_values_array = np.array(sex_controlled_significant_p_values)
    
overlapping_transcripts = len(list(set(sex_controlled_differential_transcripts) & set(differential_transcripts)))
percent_overlap = (overlapping_transcripts/len(differential_transcripts))*100
print(percent_overlap)

plt.plot(sex_controlled_beta_coefficients, -np.log10(sex_controlled_pvalues_array), '.b', label = 'Not significant')
plt.plot(sex_controlled_significant_b_coef, -np.log10(sex_controlled_significant_p_values_array), '.r', label = 'Significant')
plt.title('Volcano Plot of Differential Gene Expression by Stage \n Controlling for Sex as a Covariate')
plt.xlabel('Beta Coefficients for Stage')
plt.ylabel('-log10 (p value)')
plt.legend()
plt.savefig('volcano_plot.png')