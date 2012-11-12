#!/usr/bin/python
from PIL import Image 


def eval_fun(arg) :
	print arg
	pass

im = Image.open('oxygen.png')

pix = im.load()

old_char = ''
val = ""
for j in range(0,100) :
	#print pix[j*7,i][0]
	try :
		char_val  = chr(pix[j*7,43][0])
		#print j 
		#print char_val 
#		if char_val != old_char :
		val= val +  char_val
		#	old_char = char_val

	except:

		print val + "\n",


next = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print "".join(map(chr , next ))
