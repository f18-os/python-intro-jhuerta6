#! /usr/bin/env python3

# CS 4375 - Theory of Operating Systems
# Instructor: Dr. Eric Freudenthal

# Description of program: Takes an input file, formats it and removes punctuation, and then creates a dictionary
# with words found in the document and number of repetition of the word.

# Author: Jorge Huerta H.

# To-do: All done!

import sys        # command line arguments
import re         # regular expression tools

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]
words_master_list = []  # list of words
dictionary = {}  # stores words and instances

with open(textFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()  # get rid of newline characters
        line = line.lower()  # line to lower case
        line = re.sub('[--]', ' ', line)  # remove punctuation
        #line = re.sub(r'[,.:;]', '', line)  # NOTE: Had to remove this to pass wordCountTest.py
        # \s any whitespace character, \w any alphanumeric character
        line = re.sub(r'[^\s\w]', ' ', line)  # remove NOT common word characters. NOTE: Added this to pass wordCountTest.py
        words_master_list.extend(line.split())  # extend our list of words

for word in words_master_list:
    if word in dictionary:  # word exists in dictionary
        temp = dictionary[word]
        temp += 1  # add another instance of the word
        dictionary[word] = temp
    else:  # add word to dictionary
        dictionary[word] = 1  # populate an instance

sorted_list = sorted(dictionary)  # sort list for correct formatting

f = open(outputFname, 'w')  # open output file to write to it

for word in sorted_list:
    instances = dictionary[word]  # number of instances of the word
    f.write(word + " " + str(instances) + "\n")  # write to file

f.close()  # close the file
exit()  # exit program