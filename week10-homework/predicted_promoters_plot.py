#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

median_paper_predictions = []
median_model_predictions = []
gene_names = []
descriptions = []
gene_id = []
for i, line in enumerate(open(sys.argv[1])):
    if line.strip('"').startswith('##'):
        header = np.array(line.strip('"\r\n').split('\t'))
    elif not line.strip('"').startswith('#'):
        fields = line.strip('"\r\n').split('\t')
        median_paper_predictions.append(float(fields[4]))
        gene_id.append(fields[0])
        gene_names.append(fields[1])
        descriptions.append(fields[2])

predicted_gene_id = []
for i, line in enumerate(open(sys.argv[2])):
    if line.strip('"').startswith('##'):
        header = np.array(line.strip('"\r\n').split('\t'))
    elif not line.strip('"').startswith('#'):
        fields = line.strip('"\r\n').split('\t')
        predicted_gene_id.append(fields[0])
        median_model_predictions.append(float(fields[1]))

gene_id = np.array(gene_id)
predicted_gene_id = np.array(predicted_gene_id)


matching_ids = []
for i in gene_id:
    matching_ids.append(np.where(predicted_gene_id == i)[0][0])


matching_median_model_predictions = [median_model_predictions[i] for i in matching_ids]


cor = pearsonr(median_paper_predictions, matching_median_model_predictions)
fig, ax = plt.subplots()
ax.scatter(median_paper_predictions, matching_median_model_predictions, color = "blue", s = 0.25, alpha = 1)
ax.set_xlabel("Paper Predicted expression level, \n10-fold cross validated")
ax.set_ylabel("Model Predicted expression level (log10)")
ax.set_title("Correlationg between Paper Predicted Expression Level and Model Predicted Expression Level")
line_xs = np.linspace(max(min(matching_median_model_predictions),min(median_paper_predictions)), min(max(matching_median_model_predictions),max(median_paper_predictions)), 100)
line_ys = 0 + 1 * line_xs
ax.plot(line_xs, line_ys, color = "maroon")
ax.text(0.5,3.75, "r^2 = " + str(round(cor.statistic**2, 2)) + '\nn= ' + str(len(median_paper_predictions)))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
# plt.tight_layout()
plt.savefig('paper_model_predictions_correlation_plot.png')