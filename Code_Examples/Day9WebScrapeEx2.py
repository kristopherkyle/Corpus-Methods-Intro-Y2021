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
