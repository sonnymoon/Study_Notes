# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Given an array nums of integers, return how many of them contain an even number of digits.

# Time: O(n), Space: O(1)
class Solution(object):
	def findNumbers(self, nums):
		for i in range(len(nums)):
			nums[i] = 1 if len(str(nums[i])) % 2 == 0 else 0

		return sum(nums)
