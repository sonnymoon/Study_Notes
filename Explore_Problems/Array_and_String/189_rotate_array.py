# https://leetcode.com/problems/rotate-array/
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
	def reverse(self, nums, left, right):
		while left < right:
			temp = nums[left]
			nums[left] = nums[right]
			nums[right] = temp

			left += 1
			right -= 1

	def rotate(self, nums, k):
		length = len(nums)
		k %= length

		if length <= 1 or k == 0:
			return
		
		self.reverse(nums, 0, length - 1)
		self.reverse(nums, 0, k - 1)
		self.reverse(nums, k, length - 1)
