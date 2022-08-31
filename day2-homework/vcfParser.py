#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    info_description = {}
    info_type = {}
    format_description = {}
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0

    try:
        fs = open(fname)
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):
        if line.startswith("#"):
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            if fields[start:i].count("=") == 1:
                                name, value = fields[start:i].split('=')
                                if name == "ID":
                                    ID = value
                                elif name == "Description":
                                    desc = value
                                elif name == "Type":
                                    Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: #if not looking at header
            try:
                fields = line.rstrip().split("\t") #fill the list fields by taking columns of vcf and splitting by tabs to make them items in list
                fields[1] = int(fields[1]) #make second column and integer
                if fields[5] != ".": #if column 6 is not a .
                    fields[5] = float(fields[5]) #make column 6 a float
                info = {} #initialize dictionary info
                for entry in fields[7].split(";"): #split the string into a list of strings
                    temp = entry.split("=") #split each individual string in the list into a list of strings
                    if len(temp) == 1: #if length of the list temp is 1 
                        info[temp[0]] = None #add the item in list temp to dictionary as key and value as none
                    else: #in the case that the length of temp is not 1 
                        name, value = temp #assign first item in temp to variable name and second item in temp to variable value
                        Type = info_type[name]
                        info[name] = type_map[Type](value) #these lines populate info dictionary with the names as keys and the type of data structure associated with each name as the value
                fields[7] = info #replace info column in line 7 of fields list with info dictionary
                if len(fields) > 8: #if there are more than 8 fields
                    fields[8] = fields[8].split(":") #split field 8 by colons
                    if len(fields[8]) > 1: #if there is more than one item in the 
                        for i in range(9, len(fields)): #make variable i with values in the range between 9 and length of list fields for each iteration of for loop
                            fields[i] = fields[i].split(':') #split position i of fields at colons
                    else: #if only 1 item in list 
                        fields[8] = fields[8][0] #set the value of column 8 of fields with the first value of the list in column 8 of fields
                vcf.append(fields) # add the list fields to the list vcf
            except: #if the above code failed
                malformed += 1 #skip line and add 1 to the count of malformed lines
    vcf[0][7] = info_description #line 95-97 update vcf list with info from info line and format description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    if malformed > 0: #if there are any malformed entries
        print(f"There were {malformed} malformed entries", file=sys.stderr) #print how many malformed entries there are
    return vcf #end function and return the list vcf

if __name__ == "__main__": #if the script name used in the command line is the same as the name of this script
    fname = sys.argv[1] #assign the first command line argument to the variable fname
    vcf = parse_vcf(fname) #fill list vcf with the output of this function for the file specified in the command line
    for i in range(10):
        print(vcf[i]) #print columns of vcf in the range from 0 to 10
