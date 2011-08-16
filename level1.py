#!/usr/bin/python 

from string import maketrans 

msg = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
"""

table = maketrans("abcdefghijklmnopqrstuvwxyz" , "cdefghijklmnopqrstuvwxyzab")

url = "map"


print msg.translate(table)

print url.translate(table)

print "Testing aceedit"

