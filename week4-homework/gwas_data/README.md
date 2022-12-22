2. plink --vcf genotypes.vcf --pca 10
3. plink --vcf genotypes.vcf --freq
4. plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out CB1908_IC50_gwas_results
   plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out GS451_IC50_gwas_results
7.
CB1908 Top SNP = rs10876043
This SNP may affect the gene DIP2B which may be involved in DNA methylation. A mutation in this gene could lead to abberant methylation and transcription resulting in lymphocytopenia after administration of the drug.

GS451 Top SNP = rs7257475
This SNP may affect the gene ZNF826, which is listed as a pseudogene in the genome browser. Perhaps the reference allele could have a mutation in the promoter that prevents transcription of ZNF826 and the SNP restores the promoter sequence such that the pseudogene is expressed and its product interacts with the drug in some way to lead to lymphocytopenia.