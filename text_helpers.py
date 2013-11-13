
# This is a module of python functions
# that will help you deal with text data

import string



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
def clean_ascii(word):


	pass



# This is a function to check if the given
# input is an emoticon. Currently we
# don't support that many emoticons, but
# ultimately we will
def is_emoticon(word):
	pass
	


# This is a function to clean
# an emoticon
def clean_emoticon(word):
	pass





