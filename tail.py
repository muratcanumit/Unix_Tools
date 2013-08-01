#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sys import argv
import time

def lines (file_name):
	
   	count = 0
	for x in file_name :
      		count += 1
	file_name.seek(0)
	return count
	
if len(sys.argv) == 2:
	script, filename = argv
	
	try : 	

		file_name=open(filename)
	
	except IOError :
		print "no such a file"
	
	count = lines (file_name)
		
	j=0
	for i in file_name:
		j += 1
		if j>=count-9 and j<= count:
			print i			

	file_name.close()		

elif len(sys.argv)==4:
	script, arg_opt, linenum, filename = argv
	line_num = int(linenum)

	if arg_opt == '-n' :
		
		try:	
	
			file_name=open(filename)

		except IOError :	
			print "no such a file"
		
		count = lines (file_name)		

		j=-1
		for i in file_name:
			j += 1
			if j>=count-line_num and j<= count:
				print i		

		file_name.close()

	else :
		print "Program's exited. Give correct argument and line number."

elif len(sys.argv)==3:
	script, arg_opt, filename = argv
	if arg_opt == '-f' :
	
		try:	
	
			file_name=open(filename)

		except IOError :	
			print "no such a file"	

		count = lines (file_name)
		
		j=0
		for i in file_name:
			j += 1
			if j>=count-9 and j<= count:
				print i		

		while True :	
			line = file_name.readline()
			if not line :
				time.sleep(1)
			else:
				print line
	
		file_name.close()
	
	else:
		print "Program is exited. Give correct argument."
	
else :
	print "Program's exited. Give correct argument(s) or line number."
