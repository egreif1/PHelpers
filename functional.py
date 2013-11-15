# A file with some functional methods for python

import string


# Goes through a specified fine line by line and
# applies the supplied function to it
# named apply because of the corresponding
# R function
def apply(fun,fin):

	# open file and read it line by line
	with open(fin,"r") as file:
		for line in file:
			fun(line)


# Goes through a string and applies a function
# to each token of the string after exploding
# the string on a set delimiter
# Once again the name comes from R
def sapply(fun,line,delim):
	pass	
	# break the string into array on delimiter


	# run function on every token


# Goes through a list and applies a function
# to each element of the array
def aapply(fun,array):

	# apply function to each element
	for a in array:
		fun(a)


