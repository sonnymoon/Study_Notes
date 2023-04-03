# https://leetcode.com/explore/learn/card/array-and-string/

# Unicode (Universal Character Set) is a set of characters that comprises of formulas, symbols, and text of various languages
# There are multiple unicode encoding schemes to represent characters in 7, 8, 16, or 32 bits

# Another set of characters is ASCII (American Standard Code for Information Interchange) which does not encompass as wide a range of characters as Unicode
# The ASCII encoding schemes only represent characters in 7 or 8 bits and as such, ASCII is a subset of Unicode

# Unicode is used more often for encoding and representing characters in software
# ASCII is used for electronic communication and programming languages like HTML

# A string is an array of unicode characters
# As such, many array operations can also be applied to strings, but there are some that behave differently depending on the language
	# Some operators (i.e. "==") may behave differently depending on whether they are overloaded or not
		# Operator overloading is when the implementation of an operator is different depending on the data types of the arguments
	# Strings are immutable in some languages, meaning that they cannot be changed (i.e. changing the character at an index)
		# Because of this, the time complexity of most operations will be much longer because each character needs to be copied over

# O(n) as each character must be compared
def compare(operator_overloading_supported, string_1, string_2):
	if operator_overloading_supported:
		return string_1 == string_2
	else:
		# Use native "compare" or "equals" method of the string
		# Alternatively, loop through the strings to see if the character at that index of each string is equal to each other
		if len(string_1) != len(string_2):
			return False

		for i in range(len(string_1)):
			if string_1[i] != string_2[i]:
				return False

		return True

# O(1) if strings are mutable in the language
# O(n) if strings are immutable in the language
def substitute(mutable, string, substitute_index, new_character):
	if mutable:
		string[substitute_index] = new_character
	else:
		# Convert the string into an array
		string_array = list(string)

		string_array[substitute_index] = new_character

		string = ''.join(string_array)

		# Alternatively, concatenate the substrings before and after the index
		string = string[0:substitute_index] + new_character + string[substitute_index + 1:]

# O(1) if strings are mutable in the language
# O(n) if strings are immutable in the language and only concatenated once
# O(n^2) if strings are immutable in the language and are concatenated multiple times
def concatenate(string, number_of_times):
	concatenated_string = ''

	for i in range(number_of_times):
		concatenated_string += string

	return concatenated_string
