#!/usr/bin/env python3 #tell computer to use python interpereter

import sys #import sys module
from bed_parser import * #import parse_bed function from bed_parser.py
fname = sys.argv[1] #set first command line argument as variable fname
bed = parse_bed(fname) #parse .bed file with parse_bed function into the list bed
exons = [] #initialize list exons
for lines in bed: #work through the sublists of bed list and set them as iterable variable lines
        exons.append(lines[9]) #append the values from item 9 in each sublist to the list exons 
exons.sort() #sort the list exons
if int((len(exons))/2) == float((len(exons))/2): #if even number of genes
    print(int(((exons[int((len(exons))/2)])+(exons[int(((len(exons))/2)+1)]))/2)) #find the average number of exons for the two middle values in the list
else: #if odd number
    print(int(exons[int(((len(exons))-1)/2)])) #find the middle value in list exons