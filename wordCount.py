#! /usr/bin/env python3

# takes input, makes output, keeps track of the total the number of times each word occurs in the text file
# excluding white space and punctuation
# is case-insensitive
# print out to the output file (overwriting if it exists) the list of words sorted in descending order
# with their respective totals separated by a space, one word per line
# Nature's
# fellow-citizens
# self-evident

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

if len(sys.argv) is not 2:
    print("Correct usage: wordCount.py <input text file> <output file>")
    #exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]
words_master_list = [] # list of words
dict = {'equal':1}


with open(textFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip() # get rid of newline characters
        line = line.lower() # line to lower case
        line = re.sub('[--]', ' ', line) # remove punctuation
        line = re.sub(r'[,.:;]', '', line) # remove punctuation
        words_master_list.extend(line.split()) # extend our list of words

count = 0

for word in words_master_list:
    if word in dict:
        count += 1 #testing
        print(word)
        print(True)
        print(count)
    else:
        c = 1+1 #testing