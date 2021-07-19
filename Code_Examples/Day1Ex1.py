#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:26:02 2021

@author: kkyle2
"""

string_sent = "Rock climbing and conducting corpus analyses in Python are my favorite activities."

print(len(string_sent))

list_sent = string_sent.split(" ")

print(list_sent)

len(list_sent)

av_chars = len(string_sent)/len(list_sent)

print(av_chars)

counter = 0
for char in string_sent:
	if char == " ":
		counter += 1

print(counter)

#this is not perfect - need to ignore punctuation.
better_av_chars = (len(string_sent) - len(list_sent) -1)/len(list_sent) #number of characters - number of spaces / number of words = number of characters per word
print(better_av_chars)
