1. bwa index sacCer3.fa
2. bwa mem -t 4 -R @RG\tID:A01_09\tSM:A01_09 -o A01_09.sam sacCer3.fa A01_09.fastq
   bwa mem -t 4 -R @RG\tID:A01_11\tSM:A01_11 -o A01_11.sam sacCer3.fa A01_11.fastq
   bwa mem -t 4 -R @RG\tID:A01_23\tSM:A01_23 -o A01_23.sam sacCer3.fa A01_23.fastq
   bwa mem -t 4 -R @RG\tID:A01_24\tSM:A01_24 -o A01_24.sam sacCer3.fa A01_24.fastq
   bwa mem -t 4 -R @RG\tID:A01_27\tSM:A01_27 -o A01_27.sam sacCer3.fa A01_27.fastq
   bwa mem -t 4 -R @RG\tID:A01_31\tSM:A01_31 -o A01_31.sam sacCer3.fa A01_31.fastq
   bwa mem -t 4 -R @RG\tID:A01_35\tSM:A01_35 -o A01_35.sam sacCer3.fa A01_35.fastq
   bwa mem -t 4 -R @RG\tID:A01_39\tSM:A01_39 -o A01_39.sam sacCer3.fa A01_39.fastq
   bwa mem -t 4 -R @RG\tID:A01_62\tSM:A01_62 -o A01_62.sam sacCer3.fa A01_62.fastq
   bwa mem -t 4 -R @RG\tID:A01_63\tSM:A01_63 -o A01_63.sam sacCer3.fa A01_63.fastq
3.a. samtools sort -o A01_09.bam -O bam A01_09.sam 
   samtools sort -o A01_11.bam -O bam A01_11.sam
   samtools sort -o A01_23.bam -O bam A01_23.sam 
   samtools sort -o A01_24.bam -O bam A01_24.sam 
   samtools sort -o A01_27.bam -O bam A01_27.sam 
   samtools sort -o A01_31.bam -O bam A01_31.sam 
   samtools sort -o A01_35.bam -O bam A01_35.sam 
   samtools sort -o A01_39.bam -O bam A01_39.sam 
   samtools sort -o A01_62.bam -O bam A01_62.sam 
   samtools sort -o A01_63.bam -O bam A01_63.sam 
3.b. samtools index -b -o A01_09.bam.bai A01_09.bam
   samtools index -b -o A01_11.bam.bai A01_11.bam
   samtools index -b -o A01_23.bam.bai A01_23.bam
   samtools index -b -o A01_24.bam.bai A01_24.bam
   samtools index -b -o A01_27.bam.bai A01_27.bam
   samtools index -b -o A01_31.bam.bai A01_31.bam
   samtools index -b -o A01_35.bam.bai A01_35.bam
   samtools index -b -o A01_39.bam.bai A01_39.bam
   samtools index -b -o A01_62.bam.bai A01_62.bam
   samtools index -b -o A01_63.bam.bai A01_63.bam
4. freebayes -f sacCer3.fa -p 1 --genotype-qualities A01_11.bam.bai A01_23.bam  A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam
5. vcffilter -f "QUAL > 20" yeast.vcf > yeast_filtered.vcf
6. vcfallelicprimitives -k -g yeast_filtered.vcf > yeast_filtered_decomposed.vcf
7. snpeff ann R64-1-1.99 yeast_filtered_decomposed.vcf > yeast_filtered_decomposed_annotated.vcf
	head -n 1000 yeast_filtered_decomposed_annotated > yeast_filtered_decomposed_annotated_1000.vcf