from vcfParser import * #import parse_vcf function
random_snippet = (parse_vcf("random_snippet.vcf")) #parse random_snippet.vcf into the list random_snippet
dpSNP = (parse_vcf("dbSNP_snippet.vcf")) #parse dbSNP_snippet.vcf into the list dbSNP
SNP_dict = {} #initialize the dictionary SNP_dict
matching =[] #initialize the list matching

for i, line in enumerate(dpSNP): #make variable i that equals the index of each entry in dbSNP and variable line that equals the entry
    if i==0: #if looking at the first entry of dbSNP
        continue # skip
    else: #otherwise
        SNP_dict[line[1]]=line[2] #fill SNP dict with the entries at line index 1 as keys and the entries at line index 2 as values

for key in SNP_dict: #make variable key that matches keys in SNP_dict
    for line in random_snippet: #make variable line that matches entries in random_snippet
        if line[1] == key: # if the entry at line index 1 matches the key
            line[2] = SNP_dict[key] #set the entry at line index 2 as the value of the dictionary at that key
            matching.append(line) #append the edited line to the list matching

no_matches = ((len(random_snippet[1:]))-(len(matching))) #subtract the length of the matching list from the one less than the length of random_snippet (so as to avoid header) to find # entries that don't match
if no_matches > 0: #if there are any entries in random_snippet that don't match with those in matching
    print(f"There were {no_matches} records that do not have corresponding IDs", file=sys.stderr) #print how many entries didn't match
for i in range(len(matching)): #make variable i that equals the index of each entry in matching
    print(matching[i]) #print the value of matching at index i