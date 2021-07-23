#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:55:32 2021

@author: kkyle2
"""
#concordancing

import random
random.seed(1)

import glob
import random
import re #import regular expressions module
random.seed(1) #set seed

def concord(tok_list,target,nleft,nright):
	hits = [] #empty list for search hits

	for idx, x in enumerate(tok_list): #iterate through token list using the enumerate function. idx = list index, x = list item
		if x in target: #if the item matches one of the target items

			if idx < nleft: #deal with left context if search term comes early in a text
				left = tok_list[:idx] #get x number of words before the current one (based on nleft)
			else:
				left = tok_list[idx-nleft:idx] #get x number of words before the current one (based on nleft)

			t = x #set t as the item
			right = tok_list[idx+1:idx+nright+1] #get x number of words after the current one (based on nright)
			hits.append([left,t,right]) #append a list consisting of a list of left words, the target word, and a list of right words

	return(hits)

def concord_regex(tok_list,target_regex,nleft,nright):
	hits = [] #empty list for search hits

	for idx, x in enumerate(tok_list): #iterate through token list using the enumerate function. idx = list index, x = list item
		if re.compile(target_regex).match(x) != None: #If the target regular expression finds a match in the string (the slightly strange syntax here literally means "if it doesn't not find a match")

			if idx < nleft: #deal with left context if search term comes early in a text
				left = tok_list[:idx] #get x number of words before the current one (based on nleft)
			else:
				left = tok_list[idx-nleft:idx] #get x number of words before the current one (based on nleft)

			t = x #set t as the item
			right = tok_list[idx+1:idx+nright+1] #get x number of words after the current one (based on nright)
			hits.append([left,t,right]) #append a list consisting of a list of left words, the target word, and a list of right words

	return(hits)

def tokenize(input_string):
	tokenized = [] #empty list that will be returned
	punct_list = [".", "?","!",",","'"] #this is a sample (but incomplete!) list of punctuation characters
	replace_list = ["\n","\t"] #this is a sample (but potentially incomplete) list of items to replace with spaces
	ignore_list = [""] #This is a sample (but potentially incomplete) list if items to ignore

	for x in punct_list: #iterate through the punctuation list and replace each item with a space + the item
		input_string = input_string.replace(x," " + x)

	for x in replace_list: #iterate through the replace list and replace it with a space
		input_string = input_string.replace(x," ")

	input_string = input_string.lower() #our examples will be in English, so for now we will lower them

	input_list = input_string.split(" ") #then we split the string into a list

	#finally, we ignore unwanted items
	for x in input_list:
		if x not in ignore_list: #if item is not in the ignore list
			tokenized.append(x) #add it to the list "tokenized"

	#Then, we return the list
	return(tokenized)

def corp_conc(corp_folder,target,nhits,nleft,nright):
	hits = []

	filenames = glob.glob(corp_folder + "/*.txt") #make a list of all .txt file in corp_folder
	for filename in filenames: #iterate through filename
		text = tokenize(open(filename).read())
		#add concordance hits for each text to corpus-level list:
		for x in concord(text,target,nleft,nright): #here we use the concord() function to generate concordance lines
			hits.append(x)

	# now we generate the random sample
	if len(hits) <= nhits: #if the number of search hits are less than or equal to the requested sample:
		print("Search returned " + str(len(hits)) + " hits.\n Returning all " + str(len(hits)) + " hits")
		return(hits) #return entire hit list
	else:
		print("Search returned " + str(len(hits)) + " hits.\n Returning a random sample of " + str(nhits) + " hits")
		return(random.sample(hits,nhits)) #return the random sample

def corp_conc_regex(corp_folder,target,nhits,nleft,nright):
	hits = []

	filenames = glob.glob(corp_folder + "/*.txt") #make a list of all .txt file in corp_folder
	for filename in filenames: #iterate through filename
		text = tokenize(open(filename).read())
		#add concordance hits for each text to corpus-level list:
		for x in concord_regex(text,target,nleft,nright): #here we use the concord() function to generate concordance lines
			hits.append(x)

	# now we generate the random sample
	if len(hits) <= nhits: #if the number of search hits are less than or equal to the requested sample:
		print("Search returned " + str(len(hits)) + " hits.\n Returning all " + str(len(hits)) + " hits")
		return(hits) #return entire hit list
	else:
		print("Search returned " + str(len(hits)) + " hits.\n Returning a random sample of " + str(nhits) + " hits")
		return(random.sample(hits,nhits)) #return the random sample

def write_concord(outname, conc_list):
	outf = open(outname,"w")
	outf.write("left_context\tnode_word\tright_context") #write header (optional)
	for x in conc_list:
		left = " ".join(x[0]) #join the left context list into a string using spaces
		target = x[1] #this is the node/target word
		right = " ".join(x[2]) #join the left context list into a string using spaces
		outf.write("\n" + left + "\t" + target + "\t" + right)
	outf.flush()
	outf.close()

def write_concord_tab(outname, conc_list):
	outf = open(outname,"w")
	outf.write("left_context\tnode_word\tright_context") #write header (optional)
	for x in conc_list:
		left = "\t".join(x[0]) #join the left context list into a string using spaces
		left = left.replace('"','\\"') #to avoid issues when opening in Excel
		target = x[1] #this is the node/target word
		right = "\t".join(x[2]) #join the left context list into a string using spaces
		right = right.replace('"','\\"') #to avoid issues when opening in Excel

		outf.write("\n" + left + "\t" + target + "\t" + right)
	outf.flush()
	outf.close()

## verb forms of "run"
run_conc_25 = corp_conc("brown_single",["run","runs","ran", "running"],25,10,10)

for x in run_conc_25:
	print(x)

write_concord("run_conc.txt",run_conc_25)

## words ending in the nominalization "*ment"

ment_conc_25 = corp_conc_regex("brown_single",".*ments?$",25,10,10)
write_concord("ment_conc.txt",ment_conc_25)
write_concord_tab("ment_conc_tab.txt",ment_conc_25)

#exercise 3
ation_conc_25 = corp_conc_regex("brown_single",".*..ations?$",25,10,10)
for x in ation_conc_25:
	print(x)