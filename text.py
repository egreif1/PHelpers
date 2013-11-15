
# This is a module of python functions
# that will help you deal with text data


# dependence
import string
import imp
import os


# global variables
trivial_loaded = False
trivial = {}
states_loaded = False
states = {}


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

	# send word to lowercase and strip it of whitespace
	w = word.strip().lower()

	if (len(w) == 0):
		return ""
	return w

# A function to tell us if the string has
# quotation marks in it (useful for MYSQL)
def has_quotes(word):

	# check for single or double quotes
	try:
		string.index(word,"'")
		return True
	except ValueError:
		try:
			string.index(word,"\"")
			return True
		except ValueError:
			return False

# Removes quotes from a string
def remove_quotes(line):
	line = line.replace("\"","")
	line = line.replace("'","")
	return line

# A function that takes an array and turns it into a string
# without quotation marks
def mysql_string_from_array(array):
	
	line = string.join(array,",")
	line = remove_quotes(line)
	return line

# Function to add states to dictionary
def add_state(word):

	global states

	# get rid of whitespace
	word = word.strip()

	states[word] = 1

		
# Function to load dictionary of us states
def load_us_states():

	# have to change flag
	global states_loaded

	# load functional module
	funct = load_functional()

	# apply the add function across states file
	funct.apply(add_state,"/Users/Evan/Documents/Coding/PHelpers/states.txt")

	# change flag
	states_loaded = True	


# Function to tell you if word is a us state
def is_us_state(word):

	# check if state list has been loaded
	if (not(states_loaded)):
		load_us_states()

	# check in list for word
	try:
		states[word]
		return True
	except KeyError:
		return False

	

# Checks if a line is just one contiguous word
# or has spaces
def one_word(line):

	try:
		string.index(line," ")
		return False
	except ValueError:
		return True

# A general cleaning function for mysql databases
def mysql_clean(line):

	line = line.lower()	
	line = escape_quotes(line)
	return line


# Replaces quotes at beginning and end of a string
def remove_end_quotes(line):
	return line[1:-1]
	

# This is a function to strip non-letters from
# the beginning and end of a word.
def strip_punc_all(word):

	word = word.lower()

	# strip beginning punctuation
	word = strip_punc_end(word)	
	
	# strip ending punctuation
	word = strip_punc_start(word)

	return word
	

# Strips all punctuation from the beginning
# of a word. Assumes LOWER CASE
def strip_punc_end(word):
	
	# iteration word
	index = one_strip_punc_end(word)

	# just loop until we return word
	while(not(index == word)):
		word = index
		index = one_strip_punc_end(word)

	return index


# Helper function to strip non-letters from
# the beginning of a word
# Assumes the word is in LOWER CASE
def one_strip_punc_end(word):

	if (len(word) == 0):
		return ""

	if (not(96 < ord(word[-1])<123)):
		return(word[0:-1])
	return word


# Strips all punctuation from the start of a word
# Assumes LOWER CASE
def strip_punc_start(word):

	if (len(word) == 0):
		return ""

	# iteration word
	index = one_strip_punc_start(word)

	# just loop until we return word
	while(not(index == word)):
		word = index
		index = one_strip_punc_start(word)

	return word
		



# Helper function to strip non-letters from
# the end of a word
# Assumes the word is in LOWER CASE
def one_strip_punc_start(word):

	if (not(96<ord(word[0])<123)):
		return word[1:]
	return word



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
	functional = load_functional()

	# just apply the function across the trivial file
	functional.apply(add_trivial,"/Users/Evan/Documents/Coding/PHelpers/trivial.txt")
	

# Loads the functional module and returns it
def load_functional():
	return imp.load_source("functional","/Users/Evan/Documents/Coding/PHelpers/functional.py")


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
	






