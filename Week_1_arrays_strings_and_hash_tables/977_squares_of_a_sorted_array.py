# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Time: O(n), Space: O(n)
class Solution(object):
	def sortedSquares(self, nums):
		length = len(nums)

		result = [ 0 ] * length

		left = 0
		right = length - 1

		for i in range(length - 1, -1, -1):
			square_left = nums[left] * nums[left]
			square_right = nums[right] * nums[right]

			if square_left > square_right:
				result[i] = square_left
				left += 1
			else:
				result[i] = square_right
				right -= 1

		return result

# Explanation
# The variable "result" is initialized as an array of 0's where each index will be replaced by the squares of the numbers in the array in the correct position
# The variables "left" and "right" are used to track the indexes of the array from the left and right sides, respectively
# Each index of the array is iterated through backwards using a for loop
	# The variables "square_left" and "square_right" are the squares of the numbers at indexes "left" and "right", respectively
	# The bigger of the two values are written into "result" at the index and "left" or "right" are incremented or decremented, appropriately
# The function returns "result"
