##### Arrays #####

# An array is a collection of items or "elements"
# An array can be described by its length (the number of elements it contains) as well as its capacity (the number of elements it is able to contain)
	# Counter intuitively, the capacity of an array is often returned by its "length" attribute

# Elements can range from various data types including primitive data types and other non-primitive data structures
	# An element in an array can be accessed at its "index"

# O(1)
def access(array, access_index):
	return array[access_index]

# The three basic operations for arrays (as well as most other data structures) are insertion, deletion, and search

# Elements can be inserted into an array at any index
# Each element starting from that index is shifted to the right one index to make room for the new element
	# If the new element is inserted to the end, the existing elements do not need to be shifted

# O(1) if at the end. Otherwise O(n)
def insert(array, length, insert_index, element):
	if insert_index < length:
		for index in range(length, insert_index - 1, -1):
			array[index + 1] = array[index]
	
	array[insert_index] = element
	length += 1

	return array, length

# Similarly, elements at any index can be deleted
# Each element starting from the index after the element to delete is shifted to the left one index to replace to previous element
	# This will in turn, delete the element through replacement

# O(n)
def delete(array, length, delete_index):
	for index in range(delete_index + 1, length):
		array[index - 1] = array[index]
	
	array[length - 1] = '0'
	length -= 1

	return array, length

# The simplest way to search an array for a specific element is to check the elements at each index of the array
	# If found, the index of the element is returned; else, an indicator (usually -1) is returned

# O(n)
def search(array, length, element):
	for index in range(length):
		if array[index] == element:
			return index

	return -1

# Side Notes:
# In some languages, like Python, arrays (or lists) are automatically resizable in that the capacity is equal to the length
# Arrays can be multi-dimensional in that each element of the top-most array can be an array itself whose elements are either more nested arrays or other data types

def array_testing():
	length = 0
	array = [ '0' ] * 20

	for i in range(10):
		length += 1
		array[i] = str(i)
	
	print('BEFORE', length, array)

	access_result = access(array, 1)
	print('The element at index 1 is', access_result)

	array, length = insert(array, length, 3, 'X')

	array, length = delete(array, length, 6)

	search_result = search(array, 8)
	if search_result >= 0:
		print('The element 3 is at index', search_result)
	else:
		print('The element was not found in the array')

	print('AFTER', length, array)

# Unicode (Universal Character Set) is a set of characters that comprises of formulas, symbols, and text of various languages
# There are multiple unicode encoding schemes to represent characters in 7, 8, 16, or 32 bits

# Another set of characters is ASCII (American Standard Code for Information Interchange) which does not encompass as wide a range of characters as Unicode
# The ASCII encoding schemes only represent characters in 7 or 8 bits and as such, ASCII is a subset of Unicode

# Unicode is used more often for encoding and representing characters in software
# ASCII is used for electronic communication and programming languages like HTML

# A string is an array of unicode characters
# As such, many array operations can also be applied to strings, but there are some that behave differently depending on the language
    # The "==" operator may or may not do a proper comparison of whether two strings are the same in composition
    # Strings are immutable in some languages, meaning that they cannot be changed (i.e. changing the character at an index)

