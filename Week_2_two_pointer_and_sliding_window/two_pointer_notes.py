# https://leetcode.com/articles/two-pointer-technique/

# The "Two Pointer Technique" is the methodology of using two reference variables (pointers) while iterating through an array
# The technique is commonly used when the solution requires processing a pair or multiple pairs of elements

# Common patterns include pointers starting at opposite ends of an array or pointers that do not increment (or decrement) equally with each iteration through an array

def opposite_ends():
	array = [ 0, 1, 2, 3, 4 ]
	
	pointer_one = 0
	pointer_two = len(array) - 1

	while pointer_one < pointer_two:
		pointer_one += 1
		pointer_two -= 1

def slow_and_fast():
	# Better example would be to find a loop in a linked list
	array = [ 0, 1, 2, 3, 4 ]
	
	pointer_one = pointer_two = 0

	while pointer_two < len(array) - 1:
		pointer_one += 1
		pointer_two += 2
