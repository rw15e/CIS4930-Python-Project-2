"""
Homework 2 
CIS4930
Summer 17
Ryan Winter
rw15e
"""

from __future__ import print_function
import time 
import sys
import string
#fileContent = []
plainText = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipherText = ""

with open(sys.argv[1], 'r') as inFile:	# this reads in and saves whole file
	fileContent = inFile.read()	
	#print(inFile.read())
#print(fileContent)


print("Please enter a keyword for the mixed cipher: ")
keyWord = raw_input().upper()

editedPlainText = plainText

#editdPlainText = #holds A-Z with the keyword letters taken out

cipherText = keyWord + editedPlainText

fileContent = fileContent + keyWord
outNew = []
for z in cipherText:
	if z not in outNew:
		outNew.append(z)

outNew2 = []
for y in fileContent:
	if y not in outNew2:
		outNew2.append(y)


print("Plaintext:", plainText)
newOutput = "".join(outNew)
print("Ciphertext:", newOutput)
newOutput2 = "".join(outNew2)
print(newOutput2)

