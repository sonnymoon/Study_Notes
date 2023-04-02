# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Time: O(n), Space: O(1)
class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		consecutive_ones = max_consecutive_ones = 0

		for num in nums:
			if num == 1:
				consecutive_ones += 1
			else:
				max_consecutive_ones = max(consecutive_ones, max_consecutive_ones)
				consecutive_ones = 0
		
		return max(consecutive_ones, max_consecutive_ones)
