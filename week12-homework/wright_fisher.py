#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def calcwrightfisher(frequency, population):

    n = 2*population
    p = frequency
    allele_freq = [frequency]
    
    while p > 0 and p < 1:
        p = (np.random.binomial(n, p))/n
        allele_freq.append(p)
    return(allele_freq)
    

def plotwrightfisher(allele_freq, starting_freq, pop):
    fig, ax = plt.subplots()
    plt.plot(allele_freq, linewidth = .5)
    ax.set_xlabel("Number of Generations")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(f"Change in Allele Frequency Over Time for an Allele \n with Starting Frequency {starting_freq} and Population {pop}")
    plt.savefig(f"wrightfisher.png")

def wrightfisher(frequency,population):
    allele_frequency = calcwrightfisher(frequency = frequency, population = population)
    plotwrightfisher(allele_freq = allele_frequency, starting_freq = frequency, pop = population)

def timetofixationhist(simulations):
    generations = []
    for i in range(simulations):
        generations.append(len(calcwrightfisher(frequency=0.5, population = 100)))
    fig, ax = plt.subplots()
    plt.hist(generations)
    ax.set_xlabel("Number of Generations")
    ax.set_ylabel("Counts")
    ax.set_title(f"Variation in Time to Fixation for an Allele \n with Starting Frequency 0.5 and Population 100")
    plt.savefig(f"wrightfisherhistogram.png")
    
def timetofixationpop(population):
    generations = []
    for i in population:
        generations.append(len(calcwrightfisher(frequency=0.5, population = i)))
    fig, ax = plt.subplots()
    plt.plot(population,generations)
    plt.xscale('log')
    ax.set_xlabel("Population")
    ax.set_ylabel("Fixation Time")
    ax.set_title(f"Time to Fixation for an Allele \n with Starting Frequency 0.5 as a Function of Population Size")
    plt.savefig(f"wrightfisherpopulation.png")

def timetofixationfreq(frequency):
    simulations = 100
    generations = [[],[],[],[],[]]
    for i, freq in enumerate(frequency):
        for j in range(simulations):
            generations[i].append(len(calcwrightfisher(frequency=freq, population = 100)))
    # print(generations)
    fig, ax = plt.subplots()
    plt.violinplot(dataset=generations, positions = frequency, widths =0.1)
    ax.set_xlabel("Starting Allele Frequency")
    ax.set_ylabel("Fixation Time")
    ax.set_title(f"Time to Fixation for an Allele \n with Starting Frequency 0.5 as a Function of Population Size")
    plt.xticks(frequency)
    plt.savefig(f"wrightfisherallelefrequency.png")
    
wrightfisher(0.9,100)

timetofixationhist(1000)

timetofixationpop([100,1000,10000,100000,1000000])

timetofixationfreq([.1,.3,.5,.7,.9,])