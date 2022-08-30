#Usage: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[1] #set input filename
if len(sys.argv) > 2: #if user-specified number of lines provided
    n_lines = int(sys.argv[2]) #set the desired number of lines
else: #otherwise
    n_lines = 10 #set the desired number of lines to a default
counter = 0 #set counter of number of lines added to 0
filelines = [] #list to be filled
for line in open(filename): #for every line in the open file
    filelines.append(line) #add each line as item in list
    counter = counter + 1 #set counter to add 1
for index, line in enumerate(filelines): #for every line in the open file
    if index >= counter - n_lines: #if a desired line based on its index relative to the length of the list
        print(line.strip("\r\n")) #print the line

# Overall, great script. It does what it is supposed to, is well commented,
# And handles a default number of lines. The only comments that I have are
# about readability. It is helpful to include blank lines to break up the
# code into functional blocks. Also, longer comments are easier to read on
# their own lines. This will also help you when you write a larger script.
# Great job and keep it up! - Mike