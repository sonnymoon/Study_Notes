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
# "length" = length of the array
# "result" = array of sorted sqaures of each number
# "left" = index from the start of the array
# "right" = index from the end of the array
# for each index in "result" starting from the last index:
	# "square_left" = square of the number at "left"
	# "square_right" = square of the number at "right"
	# if "square_left" is greater than "square_right":
		# set the number at the current index of "result" to "square_left"
		# increment "left"
	# else:
		# set the number at the current index of "result" to "square_right"
		# decrement "right"
# return result
