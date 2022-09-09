#!/usr/bin/env python3 #

import sys #import module sys

def parse_bed(fname): #define function parse_bed
    malformed = 0 #set variable malformed at 0
    
    try:
        fs = open(fname, 'r') #try opening file given in command line and putting it in list fs
    except:
        raise FileNotFoundError("That file doesn’t appear to exist") #if fails raise this error
        
    bed = [] #initialize list bed
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str] #initialize list field_types
    
    for i, line in enumerate(fs): #make variable i that equals the index of each entry in list fs and variable line that equals the entry
        if line.startswith("#"): # if the line is a header
            continue #skip it
        fields = line.rstrip().split() #make list fields by stripping and splitting line
        fieldN = len(fields) #make variable fieldN which equals length of field
        if fieldN < 3 or fieldN == 10 or fieldN ==11: #if fieldN is less than 3 or equal to 10 or 11
            malformed += 1 #add 1 to malformed
            continue #then move on
        try:
            for j in range(min(len(field_types), len(fields))): #try to make variable j that equals the index of the range generated by the list with the shorter length 
                fields[j] = field_types[j](fields[j]) #make the data at index j of fields the type specified at index j of field types
                
                rbg=fields[8].split(",") #split the values of fields index 8 at commas
                rbg_values=[] #initialize list rbg_values
                if len(rbg) == 3: #if the length of an entry in rbg is 3
                    for x in rbg: #make variable x that corresponds to each entry in rbg
                        if float(x) == int(x): #if the float of the entry at that position and its integer are the same
                            rbg_values.append(int(x)) #append the integer to the list rbg_values 
            
                block_size=fields[10].split(",") #split the values of fields index 10 at commas
                block_size_values=[] #initialize list block_size_values
                for x in range(len(block_size)-1): #make variable x that corresponds to every index of block_size except the last
                    block_size_values.append(int(block_size[x])) #append the integer of block size at variable c to list block_size_values
                  
                    
                block_start=fields[11].split(",") #split the values of fields index 11 at commas
                block_start_values=[] #initialize list block_start_values
                for x in range(len(block_start)-1): #make variable x that corresponds to every index of block_start except the last
                    block_start_values.append(int(block_start[x])) #append the integer of block start at variable c to list block_start_values
            
            fields[8]=rbg_values #set the values of fields at index 8 to the values in list rbg values
            fields[10]=block_size_values #set the values of fields at index 10 to the values in list block_size_values
            fields[11]=block_start_values #set the values of fields at index 11 to the values in list block_start_values
            
            bed.append(fields) #append the edited fields to the list bed
        except: #if the code indented under try fails
            malformed +=1 #add 1 to malformed
        try:
            fields[9] = len(fields[10]) and len(fields[11]) #check if the entry at index 9 of fields matches the length of the entries at indices 10 and 11
        except: # if the code in the try statement fails
            malformed += 1 #add 1 to malformed
            
    if malformed > 0: #if there were malformed entries
        print(f"There were {malformed} malformed entries", file=sys.stderr) #print how many malformed entries there were
    fs.close() #close the file opened earlier
    return bed #return the list bed

if __name__ == "__main__": #if the name of the script in the command line matches the name of this script
    fname = sys.argv[1] #assign the first command line argument to the variable fname
    bed = parse_bed(fname) # fill the list parse using the function parse_bed on the file specified in the command line