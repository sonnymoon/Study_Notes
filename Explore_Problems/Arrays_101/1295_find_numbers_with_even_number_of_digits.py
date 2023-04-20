# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Given an array nums of integers, return how many of them contain an even number of digits.

# Time: O(n), Space: O(1)
class Solution(object):
	def findNumbers(self, nums):
		count = 0

		for num in nums:
			if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
				count += 1
		
		return count

# Explanation
# This solution only works with positive numbers whose max values are known and reasonably small
# "count" = count of numbers with an even number of digits
# iterate through the numbers of the array using a for loop
	# if the number is within the ranges of (10, 99) or (1000, 9999) or equal to 100000, increment "count"
# return "count"

# Time: O(n), Space: O(1)
class Solution(object):
	def findNumbers(self, nums):
		count = 0

		for num in nums:
			if len(str(num)) % 2 == 0:
				count += 1
		
		return count

# Explanation
# This solution works with positive numbers whose max values are unknown or known to be large
# "count" = count of numbers with an even number of digits
# iterate through the numbers of the array using a for loop
	# if the length of the number converted to string is even, increment "count"
# return "count"
