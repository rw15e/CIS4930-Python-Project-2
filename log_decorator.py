"""
Homework 2 
CIS4930
Summer 17
Ryan Winter
rw15e
"""
from __future__ import print_function
import time 
start = time.time()

#if(len(sys.argv) == 2): # if user passes in one command line argument
#	print("THERE is 1 argument")
	#with open(argv[1], "w") as givenFile:
		#givenFile.write("text to append here")
#else:
#	print("NO ARGUMENTS")
	# if no arguments then write statements to stdout

def log(param):	
	print("Calling function ", __name__, ".", sep='')	
	print("Arguments:")
	if(param == None):
		print("No arguments.")
	#else:
		
	#print arguments here
	print("Output:")
	#print outputs here
	end = time.time()
	run_time = end - start
	print("Execution time: %.5f" % run_time) #print execution time here
	print("Return value:") #print return values (or none)

	

#@log
#def scan_filea():
#	wait(20)
#	x = 5
#	x = x*x+5

