#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 19:51:56 2021

@author: kkyle2
"""

#1. Count the number of words: 
sample = """The New York Times is an American daily newspaper based in New York City with a worldwide readership. Founded in 1851, the Times has since won 130 Pulitzer Prizes, and has long been regarded within the industry as a national "newspaper of record". It is ranked 18th in the world by circulation and 3rd in the U.S. Wikipedia"""
print(sample)
sample_split = sample.split(" ") #split sample into words
print(sample_split)
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

print(clean_sample)
#2 Count the number of characters (excluding spaces and punctuation marks).
nchars = 0
for word in clean_sample:
	nchars += len(word)
print(nchars)
#3. Calculates the average number of characters per word.
nwords = len(clean_sample)
av_chars = nchars/nwords

#4. Count the number of regular past tense words.

past_tense = []
for word in clean_sample:
	if word[-2:] == "ed":
		past_tense.append(word)

print(past_tense)
print(len(past_tense))

sstring = "walked"
sstring[-2:]
