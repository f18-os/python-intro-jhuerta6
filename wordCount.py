#! /usr/bin/env python3

# CS 4375 - Theory of Operating Systems
# Instructor: Dr. Eric Freudenthal
# Description of program: Takes an input file, formats it and removes punctuation, and then creates a dictionary
# with words found in the document and number of repetition of the word.

# Author: Jorge Huerta H.

# To-do: create output file, sys.argv conditions

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess  # executing program

if len(sys.argv) is not 2:
    print("Correct usage: wordCount.py <input text file> <output file>")
    #exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]
words_master_list = []  # list of words
dictionary = {}  # stores words and instances


with open(textFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()  # get rid of newline characters
        line = line.lower()  # line to lower case
        line = re.sub('[--]', ' ', line)  # remove punctuation
        line = re.sub(r'[,.:;]', '', line)  # remove punctuation
        words_master_list.extend(line.split())  # extend our list of words

for word in words_master_list:
    if word in dictionary:  # word exists in dictionary
        temp = dictionary[word]
        temp += 1  # add another instance of the word
        dictionary[word] = temp
    else:  # add word to dictionary
        dictionary[word] = 1  # populate an instance

sorted_list = sorted(dictionary)

for word in sorted_list:
    instances = dictionary[word]
    print(word + " " + str(instances))