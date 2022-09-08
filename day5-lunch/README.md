Exercise 1.
cut -d "," -f 5,6 aau1043_dnm.csv | grep 'father' | sort -k 1 -n | uniq -c > father.txt
cut -d "," -f 1 father.txt > father_counts.txt
cut -d "," -f 5,6 aau1043_dnm.csv | grep 'mother' | sort -k 1 -n | uniq -c > mother.txt
cut -d "," -f 1 mother.txt > mother_counts.txt
awk -v OFS='\t' '{print $1, $2}' father_counts.txt > father_counts_tab_delimited.txt
awk -v OFS='\t' '{print $1, $2}' mother_counts.txt > mother_counts_tab_delimited.txt
join -1 2 -2 2 -t $'\t' father_counts_tab_delimited.txt mother_counts_tab_delimited.txt > proband_parents.tx
join -1 1 -2 1 proband_parents.txt parental_ages_delimited_sorted.txt > proband_denovo_mutations_by_parent_age.txt