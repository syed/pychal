#!/usr/bin/python 
import urllib 
import re 

nothing = "46059"

for i in range(0,400)  :
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing 
	data = urllib.urlopen(url).read()
	print data 
	result = re.search(".*and the next nothing is (\d+)$" , data )
	nothing = result.group(1)


