#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:22:24 2021

@author: kkyle2
"""
#Day9 Ex1

#https://en.wikipedia.org/wiki/Corpus_linguistics

import requests
import time
from bs4 import BeautifulSoup
from corpus_toolkit import corpus_tools as ct

cl = requests.get("https://en.wikipedia.org/wiki/Corpus_linguistics")

cl_soup = BeautifulSoup(cl.content, 'html.parser')

corpus = []
for x in cl_soup.find_all(["h1","h2","h3","p"]): #get all h1, h2, h3, and p tags
	corpus.append(x.get_text()) #get data from tags
	print(x.get_text())
corpus = "\n".join(corpus)

cl_freq = ct.frequency(ct.tokenize([corpus])) #tokenize corpus
ct.head(cl_freq)

cl_freq3 = ct.frequency(ct.tokenize([corpus],ngram = 3)) #tokenize corpus as trigrams
ct.head(cl_freq3)





#How to write .html to file:
outf = open("corp.html", "w") #create write file
outf.write(str(cl.content)) #write string version of content using srt() function
outf.flush() #flush buffer
outf.close() #close file

#Scrape a more complicated page

#http://www.koreaherald.com/view.php?ud=20210726000173

cl2 = requests.get("http://www.koreaherald.com/view.php?ud=20210726000173")

cl2_soup = BeautifulSoup(cl2.content, 'html.parser')

### First try
corpus2 = []
for x in cl2_soup.find_all(["title"]): #get title from page
	corpus2.append(x.get_text()) #get text from title tag
	print(x.get_text())
for x in cl2_soup.find_all(["div"]): #get all h1, h2, h3, and p tags
		corpus2.append(x.get_text()) #get data from tags
		print(x.get_text())
corpus2 = "\n".join(corpus2)



#Better try (using class information)
for x in cl2_soup.find_all(["div"]): #get all h1, h2, h3, and p tags
	if x.has_attr("class") == True:
		print(x["class"]) 

#Better try (using attribute information)
corpus2 = []
for x in cl2_soup.find_all(["title"]): #get title from page
	corpus2.append(x.get_text()) #get text from title tag
	print(x.get_text())
for x in cl2_soup.find_all(["div"]): #get all div tags
	if x.has_attr("class") == True: #check to see if div tag has a "class" attribute
		if "view_con_t" in x["class"]: #check to see if "view_con_t" is in list of class attributes
			corpus2.append(x.get_text()) #get text data
			print(x.get_text())
corpus2 = "\n".join(corpus2)

cl_freq2 = ct.frequency(ct.tokenize([corpus2])) #tokenize corpus
ct.head(cl_freq2)
