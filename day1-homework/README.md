# QBB2022 - Day 1 - Homework Exercises Submission=======
=======


Exercise 1.
a.
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
I get the error message above and I will address it by assigning the nuc variable within awk.
b.
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
c.
The results make sense from a biological perspective because in each case the most common variant is the most chemically similar nucleotide to the reference i.e. pyrimidines swapped for pyrimidines and purines swapped for purines.
=======
Exercise 2. 
a. Promoter regions do not appear to be clearly defined by any of the states, so we defined it as 2.
awk '{if ($4 == "2") {print}}' ~/qbb2022-answers/day1-homework/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed >> promoter.bed
bedtools intersect -a ~/qbb2022-answers/day1-homework/random_snippet.vcf -b ~/qbb2022-answers/day1-homework/promoter.bed >> new.vcf
grep -v "#" ~/qbb2022-answers/day1-homework/new.vcf | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c
   7 A
   4 G
  24 T
The most common alternate allele is T. This is consistent with general trends observed with regard to the most common alternate allele observed for Cs outside of promoter regions. I hypothesize that this is due to the chemical similarity between the two nucleotides.


