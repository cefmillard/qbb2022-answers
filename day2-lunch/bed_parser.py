#!/usr/bin/env python3

import sys

def parse_bed(fname):
    malformed = 0
    
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
        
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3 or fieldN == 10 or fieldN ==11:
            malformed += 1
            continue
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
                
                rbg=fields[8].split(",")
                rbg_values=[]
                if len(rbg) == 3:
                    for x in rbg:
                        if float(x) == int(x):
                            rbg_values.append(int(x))
            
                block_size=fields[10].split(",")
                block_size_values=[]
                for x in range(len(block_size)-1):
                    block_size_values.append(int(block_size[x]))
                  
                    
                block_start=fields[11].split(",")
                block_start_values=[]
                for x in range(len(block_start)-1):
                    block_start_values.append(int(block_start[x]))
            
            fields[8]=rbg_values
            fields[10]=block_size_values
            fields[11]=block_start_values
            
            bed.append(fields)
        except:
            malformed +=1
        try:
            fields[9] = len(fields[10]) and len(fields[11])
        except:
            malformed += 1
            
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)