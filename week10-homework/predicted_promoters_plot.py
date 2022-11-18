#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

median_paper_predictions = []
median_model_predictions = []
gene_names = []
descriptions = []
for i, line in enumerate(open(sys.argv[1])):
    if line.strip('"').startswith('##'):
        header = np.array(line.strip('"\r\n').split('\t'))
    elif not line.strip('"').startswith('#'):
        fields = line.strip('"\r\n').split('\t')
        median_paper_predictions.append(float(fields[4]))
        gene_names.append(fields[1])
        descriptions.append(fields[2])

for i, line in enumerate(open(sys.argv[2])):
    if line.strip('"').startswith('##'):
        header = np.array(line.strip('"\r\n').split('\t'))
    elif not line.strip('"').startswith('#'):
        fields = line.strip('"\r\n').split('\t')
        median_model_predictions.append(float(fields[1]))
        # gene_names.append(fields[1])
        # descriptions.append(fields[2])
print(median_model_predictions)
print(median_paper_predictions)

# cor = pearsonr(median_paper_predictions, median_model_predictions)
fig, ax = plt.subplots()
ax.scatter(median_paper_predictions, median_model_predictions, color = "blue", s = 0.25, alpha = 1)
ax.set_xlabel("Paper Predicted expression level, \n10-fold cross validated")
ax.set_ylabel("Model Predicted expression level (log10)")
line_xs = np.linspace(max(min(median_model_predictions),min(median_paper_predictions)), min(max(median_model_predictions),max(median_paper_predictions)), 100)
line_ys = 0 + 1 * line_xs
ax.plot(line_xs, line_ys, color = "maroon")
ax.text(0.5,3.75, "r^2 = " + str(round(cor.statistic**2, 2)) + '\nn= ' + str(len(median_paper_predictions)))
# for geneoi, idx in zip(genesoi, genesoilocs):
#     ax.text(k562_model_predictions[idx], k562_observations[idx], geneoi, color = 'maroon', fontweight = 'demi')
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.show()