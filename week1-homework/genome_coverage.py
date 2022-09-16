#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
np.set_printoptions(threshold=sys.maxsize)

reads = np.zeros(50000, dtype = int)

np.random.seed(1)
for i in range(len(reads)):
    reads[i] = int(np.random.randint(0, 999901))
readscount = np.bincount(reads)
print(len(readscount))
bases = np.zeros(1000000, dtype = int)
for i in range(len(readscount)):
    if readscount[i] > 0:
        for j in range(i+1, i+100):
            bases[j] += readscount[i]
n_zeros = np.count_nonzero(bases==0)
print(n_zeros)

mu = 5
x = np.arange(stats.poisson.ppf(.000001, mu), stats.poisson.ppf(0.99, mu))

fig, ax = plt.subplots()
ax.hist(bases, bins = 10, alpha = 0.5, color = 'red')
ax.set_xlabel("Coverage")
ax.set_ylabel("Frequency", color = 'red')
ax.tick_params(axis ='y', labelcolor = 'red')
ax.set_title("Frequency of Coverage after 50000 reads compared to Poisson PMF with lambda of 5")

ax2 = ax.twinx()
ax2.set_ylabel('Probability', color = 'blue')
ax2.plot(x, stats.poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax2.tick_params(axis ='y', labelcolor = 'blue')

plt.savefig('5_times_coverage_historgram.png')
plt.close(fig)





reads = np.zeros(150000, dtype = int)

np.random.seed(1)
for i in range(len(reads)):
    reads[i] = int(np.random.randint(0, 999901))
readscount = np.bincount(reads)
print(len(readscount))
bases = np.zeros(1000000, dtype = int)
for i in range(len(readscount)):
    if readscount[i] > 0:
        for j in range(i+1, i+100):
            bases[j] += readscount[i]
n_zeros = np.count_nonzero(bases==0)
print(n_zeros)

mu = 15
x = np.arange(stats.poisson.ppf(.000001, mu), stats.poisson.ppf(0.99, mu))

fig, ax = plt.subplots()
ax.hist(bases, bins = 10, alpha = 0.5, color = 'red')
ax.set_xlabel("Coverage")
ax.set_ylabel("Frequency", color = 'red')
ax.tick_params(axis ='y', labelcolor = 'red')
ax.set_title("Frequency of Coverage after 150000 reads compared to Poisson PMF with lambda of 15")


ax2 = ax.twinx()
ax2.set_ylabel('Probability', color = 'blue')
ax2.plot(x, stats.poisson.pmf(x, mu), 'bo', label='poisson pmf')
ax2.tick_params(axis ='y', labelcolor = 'blue')

plt.savefig('15_times_coverage_historgram.png')
plt.close(fig)