# Some functions for hashing in python


# Fast hash for a string
def hash1(word):

	key = 5381

	hash = 0
	for c in word:
		hash = (hash*33+ord(c)+hash)

	return hash

