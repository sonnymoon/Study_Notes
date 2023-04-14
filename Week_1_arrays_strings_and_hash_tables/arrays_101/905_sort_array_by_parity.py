# https://leetcode.com/problems/sort-array-by-parity/
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Time: O(n), Space: O(1)
class Solution(object):
	def sortArrayByParity(self, nums):
		left = 0
		right = len(nums) - 1

		while left < right:
			if nums[left] % 2 == 1 and nums[right] % 2 == 0:
				nums[left], nums[right] = nums[right], nums[left]

			left += 1 - nums[left] % 2
			right -= nums[right] % 2

		return nums

# Explanation
# The variables "left" and "right" are used to track the indexes of the array from the left and right sides, respectively
# Each index in the array are iterated through using a while loop
	# The while condition processes all the indexes while "left" is less than "right"
	# At each iteration, if the number at "left" is odd and the number at "right" is even, the number at those indexes are swapped
	# "left" and "right" are incremented or decremented, respectively, when the number at those indexes are even or odd, respectively
		# The modulo operation returns either a 0 or 1 for even or odd numbers, respectively, so the result is used to increment "left" and decrement "right"
# The function returns the array, as all numbers were swapped in-place
