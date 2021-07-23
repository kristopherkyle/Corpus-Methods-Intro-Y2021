#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:12:35 2021

@author: kkyle2
"""
import spacy
nlp = spacy.load("en_core_web_sm")
from corpus_toolkit import corpus_tools as ct

sample = "If I had to name my favorite food it would be pepperoni pizza. I really love to eat pizza because it is nutritious and delicious."

doc = nlp(sample)

for token in doc:
	print(token.text,token.lemma_,token.pos_,token.tag_, token.dep_, token.head.text)

# If if SCONJ IN mark had
# I -PRON- PRON PRP nsubj had
# had have AUX VBD advcl be
# to to PART TO aux name
# name name VERB VB xcomp had
# my -PRON- DET PRP$ poss food
# favorite favorite ADJ JJ amod food
# food food NOUN NN dobj name
# it -PRON- PRON PRP nsubj be
# would would VERB MD aux be
# be be AUX VB ROOT be
# pepperoni pepperoni NOUN NN compound pizza
# pizza pizza NOUN NN attr be
# . . PUNCT . punct be
# I -PRON- PRON PRP nsubj love
# really really ADV RB advmod love
# love love VERB VBP ROOT love
# to to PART TO aux eat
# eat eat VERB VB xcomp love
# pizza pizza NOUN NN dobj eat
# because because SCONJ IN mark is
# it -PRON- PRON PRP nsubj is
# is be AUX VBZ advcl love
# nutritious nutritious ADJ JJ acomp is
# and and CCONJ CC cc nutritious
# delicious delicious ADJ JJ conj nutritious
# . . PUNCT . punct love

pos_list = []
for token in doc:
	if token.pos_ in ["PUNCT"]:
		continue
	pos_list.append(token.text.lower() + "_" + token.pos_)
print(pos_list)