# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Time: O(n), Space: O(1)
class Solution(object):
	def sortedSquares(self, nums):
		length = len(nums)

		result = [ 0 ] * length

		left = 0
		right = length - 1

		for i in range(length - 1, -1, -1):
			if abs(nums[left]) > abs(nums[right]):
				result[i] = nums[left] * nums[left]
				left += 1
			else:
				result[i] = nums[right] * nums[right]
				right -= 1

		return result
