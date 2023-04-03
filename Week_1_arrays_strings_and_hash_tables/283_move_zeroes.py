# https://leetcode.com/problems/move-zeroes/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution(object):
	def moveZeroes(self, nums):
		length = len(nums)

		read = write = 0

		while write < length:
			if read < length:
				if nums[read] != 0:
					nums[write] = nums[read]
					read += 1
					write += 1
				else:
					read += 1
			else:
				nums[write] = 0
				write += 1
