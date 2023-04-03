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
# The array is iterated through and each number is converted to a string to check if the number of digits is even to increment "evens"
# "evens" is returned