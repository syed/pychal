#!/usr/bin/python

import pickle


#data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/peakhell.jpg").read()

file = open("banner.p")
x = pickle.load(file);
print x 
for val in x : 	
	wd=""
	for word in val :
		letter = (word[0])*word[1]
		wd+=str(letter)
	print wd 


