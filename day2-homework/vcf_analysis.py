from vcfParser import *
random_snippet = (parse_vcf("random_snippet.vcf"))
dpSNP = (parse_vcf("dbSNP_snippet.vcf"))
SNP_dict = {}
matching =[]

for i, line in enumerate(dpSNP):
    if i==0:
        continue
    else:
        SNP_dict[line[1]]=line[2]
counter = 0
for key in SNP_dict:
    for line in random_snippet:
        if line[1] == key:
            line[2] = SNP_dict[key]
            matching.append(line)

no_matches = ((len(random_snippet[1:]))-(len(matching)))
if no_matches > 0:
    print(f"There were {no_matches} records that do not have corresponding IDs", file=sys.stderr)
for i in range(len(matching)):
    print(matching[i])
        
            


#print(SNP_dict)

# for line in random_snippet:
#     if i==0:
#         continue
#     else:
#         line[2]=SNP_dict["ID"]

# for s in np.unique(pca["SEX"]):
#     pca1 = []
#     pca2 = []
#     sex[s] = [pca1, pca2]#fill with two empty lists to be populated
#     for lines in pca:
#         if s == lines[3]:
#             pca1.append(lines[5])
#             pca2.append(lines[6])
#     ax.scatter(sex[s][0], sex[s][1], label = s)
#     ax.legend()
# plt.savefig("sex_colored_pca_plot.png")
# plt.close(fig)