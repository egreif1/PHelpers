# Just a variety of useful functions for python

# load modules
import operator
import string

# checks if a string has the supplied word
def has_word(w,s):
	s = s.lower()
	try:
		s.index(w)
	except ValueError:
		return False
	return True


# this returns the index of the maximum (and its value) from a list
def get_max_tuple(a_list):

	index, value = max(enumerate(a_list), key=operator.itemgetter(1))
	return((index,value))

# method for dividing string by value
def divide_string(a,n):

	if (a == "" or n == 0):
		return ""

	a_list = a.split(",")

	length = len(a_list)
	ans = [0]*length

	for i in range(0,length):
		ans[i] = str(float(a_list[i])/float(n))


	ans = ",".join(ans)
	return ans


# method for summing two strings
# that actually representations of 
# arrays in sql
def sum_strings(a,b):

	# if either string is empty return the other
	if (a == ""):
		return b
	if (b == ""):
		return a

	# convert to arrays
	a_array = a.split(",")
	b_array = b.split(",")

	length = len(a_array)
	
	# check they have the same length
	if (not(len(b_array) == length)):
		return ""

	# sum the arrays
	sum_array = [0]*length
	for i in range(0,length):	
		sum_array[i] = str(float(a_array[i])+float(b_array[i]))

	# convert back to string
	return(",".join(sum_array))


