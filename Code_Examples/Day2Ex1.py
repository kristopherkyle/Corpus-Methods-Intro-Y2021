#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:07:44 2021

@author: kkyle2
"""
###Dictionaries ###

sample_list  = [["the",69033.45], ["of" , 36998.52],["a", 30157.43]] #list of lists
simple_list = [1,2,3,4,5,6]
sample_dict = {"the": 69033.45,"of" : 36998.52,"a": 30157.43}


sample_list[0]
sample_list[0][1]

for x in sample_list:
	if x[0] == "the":
		print(x[1])

sample_dict["the"]
sample_dict["of"]

lemma_dict = {}
lemma_dict["runs"] = "run"
lemma_dict["ran"] = "run"

lemma_dict["runs"]

### Functions ###

text = """The New York Times is an American daily newspaper based in New York City with a worldwide readership. Founded in 1851, the Times has since won 130 Pulitzer Prizes, and has long been regarded within the industry as a national "newspaper of record". It is ranked 18th in the world by circulation and 3rd in the U.S. Wikipedia"""

def text_cleaner(sample): #start with a raw text (string)
	sample_split = sample.split(" ") #split sample into words
	punctuation = [",", ".", "!", "?", "'", '"'] #this is a decent but imperfect list.
	
	clean_sample = [] #empty list for clean sample
	for word in sample_split:
		token = word
		if token[0] in punctuation: #check the first character in a word
			token = token[1:]
		if token[-1] in punctuation:  #check the last character in a word
			token = token[:-1]
		if token[-1] in punctuation: #check the last character in a word a second time (quoted speech sometimes has two punctuation marks in a row)
			token = token[:-1]
	
		clean_sample.append(token) #add cleaned toke to clean_sample list
	
	
	return(clean_sample) #return a cleaned list

smpl = "awesome!!"
smpl2 = smpl[:-1]

clean_text = text_cleaner(text)
print(clean_text)

clean_text2 = text_cleaner("I love pizza! It is my favorite food, but I can't eat it everyday. This makes me sad.")
print(clean_text2)

### In class assignment 1

#create a function that takes a name as input and prints an uplifting message

def nice_note(name_string):
	output = name_string + ", you are doing awesome today! Keep up the good work!"
	return(output)

print(nice_note("Kim"))


#extra application:
	
class_list = ["Keon Hee", "Woonhyung", "HeeJae", "Bihan", "Yue"]

def encourager(name_list):
	for name in name_list:
		print(nice_note(name)+"\n")

encourager(class_list)

### In class assignment 2

#adapted from Yue:
def num_string(a):
	word_count = len(a.split())
	print(word_count)
	
	return(word_count)

corn_pizza = num_string("Corn is not awesome on pizza")

#adapted from HeeJae:

str_split= "Corn is not awesome on pizza"

def c_string(string):
	str_split = string.split(" ") #turns string into list
	print(len(str_split)) #prints the length of list

c_string(str_split)

# Kris' Solution
def nwords(string):
	slist = string.split(" ")
	return(len(slist))

nwords("Corn is not awesome on pizza")

#### Write Files ####

outf = open("sample.txt", "w") #create empty file
outf.write("I love eating pizza because pizza is nutritious\nIs that true?")
outf.flush()
outf.close()

#### Read Files ####
read_string = open("sample.txt").read()
print(read_string)
nwords(read_string)

### bnc file to dictionary:

bnc_file = open("bnc_written_freq.txt").read()
print(bnc_file[:20])

bnc_list = bnc_file.split("\n")
print(bnc_list[:20])

bnc_freq = {}

for row in bnc_list:
	cols = row.split("\t")
	word = cols[0]
	freq = float(cols[1])
	bnc_freq[word] = freq

bnc_freq["good"]
bnc_freq["pizza"]


### Function version ###

### bnc file to dictionary:

def freq_dict(filename):
	
	bnc_file = open(filename,errors = "ignore").read()
	
	bnc_list = bnc_file.split("\n")
	
	bnc_freq = {}
	
	for row in bnc_list:
		cols = row.split("\t")
		word = cols[0]
		freq = float(cols[1])
		bnc_freq[word] = freq
	
	return(bnc_freq)

bnc2 = freq_dict("bnc_written_freq.txt")
bnc2["good"]
bnc2["pizza"]

#normed frequency
corp_size = sum(bnc_freq.values())
bnc_freq_normed = {}
for word in bnc_freq:
	bnc_freq_normed[word] = (bnc_freq[word]/corp_size) * 1000000

bnc_freq_normed["good"]
bnc_freq_normed["pizza"]

