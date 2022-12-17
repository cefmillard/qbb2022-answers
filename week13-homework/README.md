1b.  ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
	 ./krona_tab_converter.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197

1c. ktImportText -o SRR492183.krona.html -q SRR492183_krona.txt
    ktImportText -o SRR492186.krona.html -q SRR492186_krona.txt
	ktImportText -o SRR492188.krona.html -q SRR492188_krona.txt
	ktImportText -o SRR492189.krona.html -q SRR492189_krona.txt
	ktImportText -o SRR492190.krona.html -q SRR492190_krona.txt
	ktImportText -o SRR492193.krona.html -q SRR492193_krona.txt
	ktImportText -o SRR492194.krona.html -q SRR492194_krona.txt
	ktImportText -o SRR492197.krona.html -q SRR492197_krona.txt

Question 1. Lactobacillales expands until Day 4 and then contracts from Day 5 to Day 8. Bacillales contracts until Day 5 then begins to expand before contracting dramatically on Day 8. Actinobacteria is present on Day 1 then disappears entirely until Days 6 and 7 when its relativley constant, before expanding dramatically on Day 8.

Question 2. You could group them based on any overlap between their sequences to see if they were from the same organism.

2a. bwa index metagenomics_data/step0_givendata/assembly.fasta

2b. bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq >     SRR492183.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492186_1.fastq metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > SRR492186.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492188_1.fastq metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > SRR492188.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492189_1.fastq metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > SRR492189.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492190_1.fastq metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > SRR492190.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492193_1.fastq metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > SRR492193.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492194_1.fastq metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > SRR492194.sam
   bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam
   samtools sort -o SRR492183_sorted.bam -O bam SRR492183.sam 
   samtools sort -o SRR492186_sorted.bam -O bam SRR492186.sam 
   samtools sort -o SRR492188_sorted.bam -O bam SRR492188.sam 
   samtools sort -o SRR492189_sorted.bam -O bam SRR492189.sam 
   samtools sort -o SRR492190_sorted.bam -O bam SRR492190.sam 
   samtools sort -o SRR492193_sorted.bam -O bam SRR492193.sam 
   samtools sort -o SRR492194_sorted.bam -O bam SRR492194.sam 
   samtools sort -o SRR492197_sorted.bam -O bam SRR492197.sam 

2d. jgi_summarize_bam_contig_depths --outputDepth depth.txt SRR492183_sorted.bam SRR492186_sorted.bam SRR492188_sorted.bam SRR492189_sorted.bam SRR492190_sorted.bam SRR492193_sorted.bam SRR492194_sorted.bam SRR492197_sorted.bam
metabat2 -i metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins_dir/bin

Question 3. a. 6 bins
b. They represent about 5% of the assembly.
grep '>' bins_dir/bin.1.fa | wc -l
grep '>' bins_dir/bin.2.fa | wc -l
grep '>' bins_dir/bin.3.fa | wc -l
grep '>' bins_dir/bin.4.fa | wc -l
grep '>' bins_dir/bin.5.fa | wc -l
grep '>' bins_dir/bin.6.fa | wc -l
grep '>' assembly.fasta | wc -l
c. The size of each bin looks right for prokaryotic genomes.
d. To see how complete they are maybe you could try to assemble the contigs and see if there are any gaps. To see how contaminated they are you could blast the contigs and see which ones didn't match part of the same genome

Question 4. a. All 55 contigs in bin 1 correspond to the species Staphylococcus aureus. Bin 2 is Staphylococcus epidermis with all 78 contigs belonging to the genus Staphylococcus, 77 of which belonged to the species epidermis. Bin 3 contains members of the phylum Firmicutes. 2 contigs in bin 3 correspond to the order Clostridiales, 1 corresponds to the order Lactobacillales, and 5 correspond to Tissierellales. There is no clear consensus for bin 3 at the genus and species levels. Bin 4 corresponds to the genus Staphyloccocus with all 37 corresponding to this genus. 24 of these 37 contigs correspond to the species Staphylococcus haemolyticus, 7 to Staphylococcus epidermidis, and 6 to Staphylococcus aureus. All 13 of the contigs in bin 5 correspond to the species Cutibacterium avidum. All 6 of the contigs in bin 6 correspond to the species Enterococcus faecalis.
./taxonomy_bash.sh bins_dir/bin.1.fa > bin1_taxonomy_info.txt
./taxonomy_bash.sh bins_dir/bin.2.fa > bin2_taxonomy_info.txt
./taxonomy_bash.sh bins_dir/bin.3.fa > bin3_taxonomy_info.txt
./taxonomy_bash.sh bins_dir/bin.4.fa > bin4_taxonomy_info.txt
./taxonomy_bash.sh bins_dir/bin.5.fa > bin5_taxonomy_info.txt
./taxonomy_bash.sh bins_dir/bin.6.fa > bin6_taxonomy_info.txt
cut -d ';' -f 5 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin1_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 5 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin2_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 5 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin3_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 5 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin4_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 5 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin5_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 5 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 6 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 7 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 8 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 9 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 10 bin6_taxonomy_info.txt| sort | uniq -c
cut -d ';' -f 11 bin6_taxonomy_info.txt| sort | uniq -c

b. You could use blast on each contig in the bin and check the percent sequence identity and see what species had the closest sequence.
