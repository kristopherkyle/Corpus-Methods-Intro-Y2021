#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:41:42 2021

@author: kkyle2
"""
import requests
import time
from bs4 import BeautifulSoup
from corpus_toolkit import corpus_tools as ct


#Get all URLS from "Overviews" Section at "https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences"

wiki = requests.get("https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences")

wiki_soup = BeautifulSoup(wiki.content, 'html.parser')

wiki_urls = []
for x in wiki_soup.find_all(["a"]): #get title from page
	if x.has_attr("href") == True: #check to see if a tag has a "href" attribute
		wiki_urls.append(x["href"])


### First, get all URLS in introduction and "overview"
wiki_urls = []
for x in wiki_soup.find_all(["a"]): #get title from page
	if x.has_attr("href") == True: #check to see if a tag has a "href" attribute
		if ":" in x["href"]:
			continue
		if "Outline" in x["href"]:
			continue
		if "List" in x["href"]:
			continue
		if x["href"][:5] != "/wiki":
			continue
		if "Main_Page" in x["href"]:
			continue
		wiki_urls.append("https://en.wikipedia.org/" + x["href"])
		
		if x["href"] == "/wiki/Space_transport": #if we get to the end of the list
			break #stop the for loop
print(len(wiki_urls))
#refine list (some links are repeated)
wiki_urls = list(set(wiki_urls))
print(len(wiki_urls))

#collect corpus data
wiki_corpus = [] #holder for entire corpus
for link in wiki_urls[:5]:
	wiki_page = [] #holder for page
	time.sleep(1) #pause between requests!
	print("Processing: " + link)
	page = requests.get(link) #download .html
	soup = BeautifulSoup(page.content, 'html.parser') #parse html page
	for text in soup.find_all(["h1","h2","h3","p"]): #grab headers and text
		wiki_page.append(text.get_text())
	wiki_corpus.append("\n".join(wiki_page)) #combine list items into a single string and add text data to wiki_corpus list

#complete initial corpus analysis
wiki_freq = ct.frequency(ct.tokenize(wiki_corpus))
ct.head(wiki_freq)
sum(wiki_freq.values())



#collect corpus data
wiki_corpus = [] #holder for entire corpus
for link in wiki_urls:
	wiki_page = [] #holder for page
	time.sleep(1) #pause between requests!
	print("Processing: " + link)
	page = requests.get(link) #download .html
	soup = BeautifulSoup(page.content, 'html.parser') #parse html page
	for text in soup.find_all(["h1","h2","h3","p"]): #grab headers and text
		wiki_page.append(text.get_text())
	wiki_corpus.append("\n".join(wiki_page)) #combine list items into a single string and add text data to wiki_corpus list

#complete initial corpus analysis
wiki_freq = ct.frequency(ct.tokenize(wiki_corpus))
ct.head(wiki_freq)
sum(wiki_freq.values())


wiki_urls = []
for x in wiki_soup.find_all(["a"]): #get title from page
	if x.has_attr("href") == True: #check to see if a tag has a "href" attribute
		if ":" in x["href"]:
			continue
		wiki_urls.append("https://en.wikipedia.org/" + x["href"])
