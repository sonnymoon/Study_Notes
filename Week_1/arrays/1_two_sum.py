# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		# Brute force
		for i in range(len(nums)):
			for j in range(len(nums)):
				if nums[i] + nums[j] == target and i != j:
					return [ i, j ]

		# Hash-Map
		differences = {}

		for index, num in enumerate(nums):
			if num in differences:
				return [ differences[num], index ]
			else:
				differences[target - num] = index