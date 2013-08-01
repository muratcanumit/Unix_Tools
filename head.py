#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sys import argv

if len(sys.argv) == 2:
	script, filename = argv
	
	try : 	
		
		file_name=open(filename)

	except IOError :	
		print "no such a file"

	i=1
	while i<=10 : 
		print file_name.readline()
		i = i+1	

	file_name.close()		

elif len(sys.argv)==4:
	script, arg_opt, linenum, filename = argv
	line_num = int(linenum)
	if arg_opt == '-n' :
	
		try :

			file_name=open(filename)
		except IOError :	
			print "no such a file"
		
		i=1	
		while i<=line_num : 
			print file_name.readline()
			i = i+1		

		file_name.close()
	else :
		print "Program is exited. Give correct argument(s)."

else :
	print "Program is exited. Give correct argument(s)."
