#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:47:28 2021

@author: kkyle2
"""
import math #for logarithmic transformation
import glob #for grabbing filenames
import operator #for dictionary sorting

def splitter(input_string): #presumes that the list is tab-delimitted
	output_list = []
	#insert code here
	for x in input_string.split("\n")[1:]: #iterate through sample string split by "\n", skip header row
		cols = x.split("\t") #split the item by "\t"
		word = cols[0] #the first item will be the word
		freq = cols[1] #the second will be the frequency value
		output_list.append([word,freq]) #append the [word, freq] list to the output list

	return(output_list)

def freq_dicter(input_list):
	output_dict = {}
	#insert code here
	for x in input_list: #iterate through list
		word = x[0] #word is the first item
		freq = float(x[1]) #frequency is second item (convert to float using float())
		output_dict[word] = freq #assign key:value pair

	return(output_dict)

def file_freq_dicter(filename):
	#out_dict = {} #if you use the previously defined function freq_dicter() this is not necessary
	spreadsheet = open(filename).read() #open and read the file here
	split_ss = splitter(spreadsheet)#split the string into rows
	out_dict = freq_dicter(split_ss)#iterate through the rows and assign the word as the key and the frequency as the value

	return(out_dict)

def safe_divide(numerator,denominator): #this function has two arguments
	if denominator == 0: #if the denominator is 0
		output = 0 #the the output is 0
	else: #otherwise
		output = numerator/denominator #the output is the numerator divided by the denominator

	return(output) #return output

def word_counter(low): #list of words
	nwords = len(low)
	return(nwords)

def frequency_count(tok_text,freq_dict):
	freq_sum = 0
	word_sum = 0
	for x in tok_text:
		if x in freq_dict: #if the word is in the frequency dictionary
			freq_sum += math.log(freq_dict[x]) #add the (logged) frequency value to the freq_sum counter
			word_sum += 1 #add one to the word_sum counter
		else:
			continue #if the word isn't in the frequency dictionary, we will ignore it in our index calculation

	return(safe_divide(freq_sum,word_sum)) #return average (logged) frequency score for words in the text

def lexical_diversity(tok_text,window_length = 50): #this is for moving average type token ratio (TTR). See Covington et al., 2010; Kyle et al. (2020); Zenker & Kyle (2020)
	if len(tok_text) < (window_length + 1):
		ma_ttr = safe_divide(len(set(tok_text)),len(tok_text))

	else:
		sum_ttr = 0
		denom = 0
		for x in range(len(tok_text)):
			small_text = tok_text[x:(x + window_length)]
			if len(small_text) < window_length:
				break
			denom += 1
			sum_ttr+= safe_divide(len(set(small_text)),float(window_length))
		ma_ttr = safe_divide(sum_ttr,denom)

	return ma_ttr

def tokenize(input_string): #input_string = text string
	tokenized = [] #empty list that will be returned

	##### CHANGES TO CODE HERE #######
	#these are the punctuation marks in the Brown corpus + '"'
	punct_list = ['-',',','.',"'",'&','`','?','!',';',':','(',')','$','/','%','*','+','[',']','{','}','"']

	#this is a sample (but potentially incomplete) list of items to replace with spaces
	replace_list = ["\n","\t"]

	#This is a sample (but potentially incomplete) list if items to ignore
	ignore_list = [""]

	##### CHANGES TO CODE HERE #######
	#iterate through the punctuation list and delete each item
	for x in punct_list:
		input_string = input_string.replace(x, "") #instead of adding a space before punctuation marks, we will delete them (by replacing with nothing)

	#iterate through the replace list and replace it with a space
	for x in replace_list:
		input_string = input_string.replace(x," ")

	#our examples will be in English, so for now we will lower them
	#this is, of course optional
	input_string = input_string.lower()

	#then we split the string into a list
	input_list = input_string.split(" ")

	for x in input_list:
		if x not in ignore_list: #if item is not in the ignore list
			tokenized.append(x) #add it to the list "tokenized"

	return(tokenized)

def list_reader(filename):
	text_list = open(filename).read().split("\n")
	return(text_list)



def list_reader(filename):
	outlist = [] #list
	text = open(filename).read().split("\n") #open, split file
	for x in text:
		if len(x) > 0:
			outlist.append(x)
	return(outlist)

pos_words = list_reader("positive_words.txt")
print(pos_words[-1]) # Check last word
print(pos_words[0]) #check first_word

neg_words = list_reader("negative_words.txt")
print(neg_words[-1]) # Check last word
print(neg_words[0]) #check first_word

sample = "this is an awesome class I love it".lower().split()

def list_counter(tok_text, lname):
	lwords = 0
	nwords = 0
	
	for word in tok_text:
		if word in lname:
			#print(word)
			lwords += 1
		nwords += 1
	
	return(safe_divide(lwords,nwords))

list_counter(sample,pos_words)
	

def text_processor(folder,outname): #folder name, name of output file
	corp_dict = {} #dictionary to store all data (not absolutely necessary, but potentially helpful)
	outf = open(outname,"w") #create output file
	outf.write("\t".join(["filename","nwords","av_freq","mattr"])) #write header
	filenames = glob.glob(folder + "/*") #get filenames in folder

	for filename in filenames: #iterate through filenames
		print(filename)
		text_d = {} #create text dictionary to store indices for each text
		simple_fname = filename.split("/")[-1] #get last part of filename
		text = tokenize(open(filename, errors = "ignore").read()) #read file and tokenize it

		#add data to the text dictionary:
		text_d["filename"] = simple_fname
		text_d["nwords"] = word_counter(text) #calculate number of words
		text_d["av_freq"] = frequency_count(text,brown_freq) #calculate average frequency
		text_d["mattr"] = lexical_diversity(text)

		### add more stuff to dictionary here as needed ###

		#add text dictionary to corpus dictionary (not absolutely necessary, but potentially helpful)
		corp_dict[simple_fname] = text_d

		out_line = [text_d["filename"],str(text_d["nwords"]),str(text_d["av_freq"]),str(text_d["mattr"])] #create line for output, make sure to turn any numbers to strings
		outf.write("\n" + "\t".join(out_line)) #write line

	outf.flush() #flush buffer
	outf.close() #close_file

	return(corp_dict)

#add indices
def text_processor2(folder,outname): #folder name, name of output file
	corp_dict = {} #dictionary to store all data (not absolutely necessary, but potentially helpful)
	outf = open(outname,"w") #create output file
	outf.write("\t".join(["filename","nwords","av_freq","mattr","pos_prop","neg_prop"])) #write header
	filenames = glob.glob(folder + "/*") #get filenames in folder

	for filename in filenames: #iterate through filenames
		print(filename)
		text_d = {} #create text dictionary to store indices for each text
		simple_fname = filename.split("/")[-1] #get last part of filename
		text = tokenize(open(filename, errors = "ignore").read()) #read file and tokenize it

		#add data to the text dictionary:
		text_d["filename"] = simple_fname
		text_d["nwords"] = word_counter(text) #calculate number of words
		text_d["av_freq"] = frequency_count(text,brown_freq) #calculate average frequency
		text_d["mattr"] = lexical_diversity(text)
		text_d["pos_prop"] = list_counter(text,pos_words)
		text_d["neg_prop"] = list_counter(text,neg_words)

		### add more stuff to dictionary here as needed ###

		#add text dictionary to corpus dictionary (not absolutely necessary, but potentially helpful)
		corp_dict[simple_fname] = text_d

		out_line = [text_d["filename"],str(text_d["nwords"]),str(text_d["av_freq"]),str(text_d["mattr"]),str(text_d["pos_prop"]),str(text_d["neg_prop"])] #create line for output, make sure to turn any numbers to strings
		outf.write("\n" + "\t".join(out_line)) #write line

	outf.flush() #flush buffer
	outf.close() #close_file

	return(corp_dict)

nict = text_processor2("NICT_JLE_Cleaned", "nict_processed.txt")
sample = "this is an awesome class I love it".lower().split()

brown_freq = file_freq_dicter("brown_freq_2020-11-19.txt")
