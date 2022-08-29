# QBB2022 - Day 1 - Lunch Exercises Submission

1. I’m excited to learn how to organize and analyze large data sets.
=======
2.
b. ~62 exons per gene. 
wc -l genes.chr21.bed wc -l exons.chr21.bed. 
c. I would map the exons to their corresponding genes based on the location columns. Then I would sort based on the number of exons per gene, then use wc to determine the length of the list, and then use head for half that list and then use the last value returned by head for the median.