# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
# Return the leftmost pivot index.
# If no such index exists, return -1.

class Solution(object):
	def pivotIndex(self, nums):
		length = len(nums)

		left = 0
		right = sum(nums)

		for i in range(length):
			right -= nums[i]

			if left == right:
				return i
			else:
				left += nums[i]
		
		return -1

# Explanation
# The variables "left" and "right" are used to track the sum of the numbers to the left and right, respectively, of the current index
	# "left" is initialized as 0 and "right" is initialized to the sum of all numbers in the array
# The indexes of the array are iterated through using a for loop
	# The number at each index is subtracted from "right" as the right sum is not inclusive of the current number
	# If "left" and "right" are equal, the function returns the index as it is a pivot index by definition
	# Otherwise, the current number is added to "left" and the for loop continues
# When the for loop completes without returning the pivot index, the function returns -1
