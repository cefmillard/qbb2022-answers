#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

pca = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["ID_1", "ID_2", "PCA_1", "PCA_2", "PCA_3"])

fig, ax = plt.subplots() #create a figure and axes
ax.scatter(pca["PCA_1"], pca["PCA_2"])
ax.set_xlabel("PCA_1")
ax.set_ylabel("PCA_2")
plt.savefig("ex2_a.png")
plt.close(fig)

fig2, ax = plt.subplots()
ax.scatter(pca["PCA_1"], pca["PCA_3"])
ax.set_xlabel("PCA_1")
ax.set_ylabel("PCA_3")
plt.savefig("ex2_B.png")
plt.close(fig2)