#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

pca = np.genfromtxt("plink_integrated_joined.txt", dtype = None, encoding = None, names = ["ID_1", "POP", "SUPER", "SEX", "ID_2", "PCA_1", "PCA_2", "PCA_3"])
sex = {}
super = {}
pop = {}

fig, ax = plt.subplots() #create a figure and axes

for s in np.unique(pca["SEX"]):
    pca1 = []
    pca2 = []
    sex[s] = [pca1, pca2]#fill with two empty lists to be populated
    for lines in pca:
        if s == lines[3]:
            pca1.append(lines[5])
            pca2.append(lines[6])
    ax.scatter(sex[s][0], sex[s][1], label = s)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.legend()
plt.savefig("ex3_a.png")
plt.close(fig)

fig, ax = plt.subplots()

for s in np.unique(pca["SUPER"]):
    pca1 = []
    pca2 = []
    super[s] = [pca1, pca2]#fill with two empty lists to be populated
    for lines in pca:
        if s == lines[2]:
            pca1.append(lines[5])
            pca2.append(lines[6])
    ax.scatter(super[s][0], super[s][1], label = s)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.legend()
plt.savefig("ex3_b.png")
plt.close(fig) 

fig, ax = plt.subplots()

for s in np.unique(pca["POP"]):
    pca1 = []
    pca2 = []
    pop[s] = [pca1, pca2]#fill with two empty lists to be populated
    for lines in pca:
        if s == lines[1]:
            pca1.append(lines[5])
            pca2.append(lines[6])
    ax.scatter(pop[s][0], pop[s][1], label = s)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.legend()
plt.savefig("ex3_c.png")
plt.close(fig)