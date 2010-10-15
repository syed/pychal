#!/usr/bin/python

import os 
import re
import zipfile


zip =  zipfile.ZipFile("channel.zip")
start_file = "90052.txt"
comm = [] 
while True : 
	try :
		data = open(start_file).read()
		print data
		res = re.search("Next nothing is (\d+)",data)
		info = zip.getinfo(start_file)
		comm.append(info.comment)
		start_file = res.group(1) + ".txt" 
	except :

		for w in comm :
			print w,
			#break
