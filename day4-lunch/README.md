# QBB2022 - Day 4 - Lunch Exercises Submission
1.
a. 
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
b. open the files and look at them, make a script that compares whether their contents are the same (I don't know if metadata like when the files are recorded is included in the contents of the file, but if they were I could tell the computer to ignore parts of the file that correlate with that metadata and see if the other contents of the files match)
c.I found the gene types "IG V", "IG D", and "IG J" becuase you could look at changes in the presence of regions correlating with these gene types to see how VDJ recombination has occurred in certain people i.e. the length of these regions might change or some might be absent in cells that have undergone VDJ recombination.
2. Most genes don't have very many alleles.
3.
SYNOPSIS
     bxlab/cmdb-plot-vcfs -- Scripts in this directory extract information contained in .gtf files into several .bed files that correlate with different genomic elements (i.e. protein coding regions, unprocessed pseudogenes, etc.). These .bed files are then used to produce .vcf files which are used to plot the frequencies of allele counts in these regions.

USAGE
     bash do_all.sh <.vcf file> <.gtf file>

DEPENDENCIES
     UNIX, bedtools, python, sys, matplotlib.pyplot, numpy

DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to find entries in the .gtf file that include chromosome of interest then put them in a new chromosome specific .gtf file
		 - Use a for loop in tandem with grep and awk to iterate through different gene types of interest and find entries in the chromosome specific .gtf file that include those data types, then extract info from columns of interest into .bed file if those entries have "gene" in column three
		 - use the same technique with "exon" instead of gene in the third column to find exons and then put them in a .bed file 
		 - use bedtools intersect with a .vcf file to intersect these regions and output a .vcf file for later use
	 2. Create plots of Allele Count frequencies in these regions
	 	 -Run plot_vcf_ac.py python script
		 -import modules
		 -open one of the vcfs generated in step 1.
		 -parse vcf file with a focus on pulling out allele count values
		 -append allele count values into list
		 -make list into numpy array
		 -log transform the array
		 -plot the frequency of allele counts on a histogram
		 -save the plots as .png files
		 
OUTPUT
	##fileformat=VCFv4.3
	##FILTER=<ID=PASS,Description="All filters passed">
	##fileDate=31052018_15h52m43s
	##source=IGSRpipeline
	##reference=ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa
	##FORMAT=<ID=GT,Number=1,Type=String,Description="Phased Genotype">
	##contig=<ID=chr21>
	##INFO=<ID=AF,Number=A,Type=Float,Description="Estimated allele frequency in the range (0,1)">
	##INFO=<ID=AC,Number=A,Type=Integer,Description="Total number of alternate alleles in called genotypes">
	##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of samples with data">
	##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">
	##INFO=<ID=EAS_AF,Number=A,Type=Float,Description="Allele frequency in the EAS populations calculated from AC and AN, in the range (0,1)">
	##INFO=<ID=EUR_AF,Number=A,Type=Float,Description="Allele frequency in the EUR populations calculated from AC and AN, in the range (0,1)">
	##INFO=<ID=AFR_AF,Number=A,Type=Float,Description="Allele frequency in the AFR populations calculated from AC and AN, in the range (0,1)">
	##INFO=<ID=AMR_AF,Number=A,Type=Float,Description="Allele frequency in the AMR populations calculated from AC and AN, in the range (0,1)">
	##INFO=<ID=SAS_AF,Number=A,Type=Float,Description="Allele frequency in the SAS populations calculated from AC and AN, in the range (0,1)">
	##INFO=<ID=VT,Number=.,Type=String,Description="indicates what type of variant the line represents">
	##INFO=<ID=EX_TARGET,Number=0,Type=Flag,Description="indicates whether a variant is within the exon pull down target boundaries">
	##INFO=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth; some reads may have been filtered">
	#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  HG00096 HG00097 HG00099 HG00100 HG00101 HG00102 HG00103 HG00104 HG00105 HG00106 HG00107 HG00108 HG00109 
	chr21   10540891        .       G       A       .       PASS    AC=184;AN=5096;DP=105570;AF=0.04;EAS_AF=0;EUR_AF=0;AFR_AF=0.13;AMR_AF=0.02;SAS_AF=0;VT=SNP;NS=2548      GT      
	chr21   10569983        .       C       T       .       PASS    AC=22;AN=5096;DP=143937;AF=0;EAS_AF=0;EUR_AF=0;AFR_AF=0.02;AMR_AF=0;SAS_AF=0;VT=SNP;NS=2548     GT      0|0     

	