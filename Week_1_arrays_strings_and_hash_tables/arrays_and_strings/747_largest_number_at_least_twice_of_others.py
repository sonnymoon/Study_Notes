# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.

# Time: O(n), Space: O(1)
class Solution(object):
	def dominantIndex(self, nums):
		first = second = result = -1

		for i in range(len(nums)):
			num = nums[i]

			if num > first:
				first, second = num, first
				result = i
			elif num > second:
				second = num
		
		return result if first >= second * 2 else -1
