# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Given an array nums of integers, return how many of them contain an even number of digits.

# Time: O(n), Space: O(1)
class Solution(object):
	def findNumbers(self, nums):
		evens = 0

		for num in nums:
			if len(str(num)) % 2 == 0:
				evens += 1

		return evens

# Explanation
# The variable "evens" is used to track the count of numbers with even number of digits
# Each number in the array is iterated through using a for loop
	# If the number converted to a string has an even length, "evens" is incremented
# When the for loop completes, the function returns "evens"
