#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("proband_denovo_mutations_by_parent_age_tab_delimited.txt", delimiter = "\t", dtype = None, encoding = None, names = ["Proband_ID", "Paternal_Mutations", "Maternal_Mutations", "Paternal_Age", "Maternal_Age"])

fig, ax = plt.subplots()
ax.scatter(df["Maternal_Age"], df["Maternal_Mutations"])
ax.set_xlabel("Maternal Age")
ax.set_ylabel("Maternal Mutations")
ax.set_title("Offspring De Novo Mutations of Maternal Origin vs Maternal Age")
plt.savefig("ex2_a.png")
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(df["Paternal_Age"], df["Paternal_Mutations"])
ax.set_xlabel("Paternal Age")
ax.set_ylabel("Paternal Mutations")
ax.set_title("Offspring De Novo Mutations of Paternal Origin vs Paternal Age")
plt.savefig("ex2_b.png")
plt.close(fig)

maternal_model = smf.ols(formula = "Maternal_Mutations ~ 1 + Maternal_Age", data = df).fit()
print(maternal_model.summary())

paternal_model = smf.ols(formula = "Paternal_Mutations ~ 1 + Paternal_Age", data = df).fit()
print(paternal_model.summary())

fig, ax = plt.subplots()
ax.hist(df["Maternal_Mutations"], alpha = 0.5, label = "Maternal")
ax.hist(df["Paternal_Mutations"], alpha = 0.5, label = "Paternal")
ax.set_xlabel("Number of De Novo Mutations")
ax.set_ylabel("Frequency")
ax.set_title("De Novo Mutations by Parental Origin")
ax.legend()
plt.savefig("ex2_c.png")


print(stats.ttest_ind(df["Maternal_Mutations"],df["Paternal_Mutations"]))

new_data = df[0]
new_data.fill(0)
new_data['Paternal_Age'] = 50.5
print(paternal_model.predict(new_data))