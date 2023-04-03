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
# The array is read from either side until an odd number on the left side and an even number on the right side are found
# When these conditions are met, the numbers switch places and the loop continues.
# The entire process can be done in-place as numbers are switching places and does not need to be operated on afterwards.
