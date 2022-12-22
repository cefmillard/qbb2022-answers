# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0.75 + 1 = 9.75 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * --> +1
  * Alternatively, you could employ a `for` loop in bash:
  ```
  for ID in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63; do
  	bwa mem -t 4 -R "@RG\tID:${ID}\tSM:${ID}"  sacCer3.fa ${ID}.fastq > aln_${ID}.sam
    samtools sort -o ${ID}.bam -O bam ${ID}.sam
    samtools index -b -o ${ID}.bam.bai ${ID}.bam
  done
  ```

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1

4. variant call with freebayes

  * --> +1

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * --> +1
  * fantastic way of getting the uniq effects and the corresponding counts for the bar plot!

9. 4 panel plot (0.25 points each panel)

  * --> +0.75, the allele frequency and the genotype quality plots are the same. Looks like you plotted `genotype_organized` for both `ax[0,1]` and `ax[1,0]`.

10. 1000 line vcf

  * --> +1
