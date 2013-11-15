
# This is a module of python functions
# that will help you deal with text data


# dependence
import string
import imp
import os


# global variables
trivial_loaded = False
trivial = {}


# This method tests if a string is
# ascii (uppercase or lowercase)
def is_ascii(word):

	try:
		word.decode('ascii')
	except UnicodeDecodeError:
		return(False)

	return(True)


# This method tests for an unbroken
# block of ascii letters
def is_word(word):
	w = word.lower()
	return(all( 96<ord(c)<123 for c in w))


# This is a function to clean
# a word and return an ascii string
# Use case: you think the word is ascii
# and want ending punctuation stripped from it
def clean_word(word):

	# send word to lowercase and strip it
	w = word.strip().lower()

	if (len(w) == 0):
		return ""

	# check if last character is a letter
	if (not(96 < ord(w[-1]) < 123)):
		return w[0:-1]
	return w
	



# This is a function to check if the given
# input is an emoticon. Currently we
# don't support that many emoticons, but
# ultimately we will
def is_emoticon(word):

	# check for smilies
	if (word == ":)"):
		return True
	elif (word == ":/"):
		return True
	elif (word == ":("):
		return True
		
	

# Adds a word to the trivial dictionary
def add_trivial(word):

	# declare that we will change global variable
	global trivial;

	# strip whitespace
	word = word.strip()

	# add entry to dictionary
	trivial[word] = 1



# Loads the set of trivial words in the
# containing directory
def load_trivial():

	# import functional
	functional = imp.load_source("functional","/Users/Evan/Documents/Coding/PHelpers/functional.py")

	# just apply the function across the trivial file
	functional.apply(add_trivial,"/Users/Evan/Documents/Coding/PHelpers/trivial.txt")
	




# This is a functio to determine whether a
# given word is trivial, or should be
# considered significant
def is_trivial(word):

	# switch to lowercase
	word = word.lower()

	# check that we've loaded the trivial list
	if (not(trivial_loaded)):
		load_trivial()

	# now check if the word is trivial
	try:
		trivial[word]
	except KeyError:
		return False
	return True
	






