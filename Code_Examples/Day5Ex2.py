#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:02:29 2021

@author: kkyle2
"""
#work with corpus toolkit

from corpus_toolkit import corpus_tools as ct

tagged_brown = ct.tag(ct.ldcorpus("brown_single"))
ct.write_corpus("tagged_brown_single",tagged_brown) #the first argument is the folder where the tagged files will be written
tagged_freq = ct.frequency(ct.reload("tagged_brown_single"))
ct.head(tagged_freq, hits = 10)

collocates = ct.collocator(ct.tokenize(ct.ldcorpus("brown_single")),"go",stat = "MI")
ct.head(collocates, hits = 10)

collocatestagged= ct.collocator(ct.reload("tagged_brown_single"),"run_VERB",stat = "MI")
ct.head(collocatestagged, hits = 10)
