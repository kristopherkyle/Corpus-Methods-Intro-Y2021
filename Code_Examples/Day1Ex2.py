#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:30:29 2021

@author: kkyle2
"""

a = "This is an awesome sample sentence"

b = a.split(" ")

for x in b:
	print(x)

c = []

for x in b:
	if x[-1] == "e":
		c.append(x)

print(c)

word = "pizza"

