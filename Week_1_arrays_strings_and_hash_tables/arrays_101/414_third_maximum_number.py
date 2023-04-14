# https://leetcode.com/problems/third-maximum-number/
# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

# Time: O(n), Space: O(1)
class Solution(object):
	def thirdMax(self, nums):
		first = None
		second = None
		third = None

		for num in nums:
			if num == first or num == second or num == third:
				continue

			if not first or num > first:
				first, second, third = num, first, second
			elif not second or num > second:
				second, third = num, second
			elif not third or num > third:
				third = num

		return third if third is not None else first
	
# Explanation
# The variables "first", "second", and "third", are used to track the first, second, and third maximum numbers in the array
	# Each of these variables are initialized to be "None" until a respective maximum is found
# Each number in the array is iterated through using a for loop
	# If the number is already the same as "first", "second", or "third" it is ignored as no two maximums can have the same value
	# If "first" is not already assigned or the number is greater than "first", "first" is assigned to the number and the maximums are shifted down
	# Else if "second" is not already assigned or the number is greater than "second", "second" is assigned to the number and its maximum is shifted down
	# Else if "third" is not already assigned or the number is greater than "third", "third" is assigned to the number
# After the iterations, if "third" is not "None" the function returns "third", else the function returns "first"
