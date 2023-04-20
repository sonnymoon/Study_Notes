# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

class Solution(object):
	def minSubArrayLen(self, target, nums):
		length = len(nums)

		slow = 0
		fast = 0

		sum = 0
		min_subarray = length

		while fast < length:
			print(slow, fast, sum, min_subarray)
			if sum < target:
				sum += nums[fast]
				fast += 1

			else:
				min_subarray = min(fast - slow, min_subarray)

				if min_subarray == 1:
					return 1

				sum -= nums[slow]
				slow += 1
		
		if min_subarray == length:
			return 0
		else:
			return min_subarray

class Solution(object):
	def minSubArrayLen(self, target, nums):
		slow = 0
		fast = 0
		sum = 0
		min_subarray = 0

		while fast < len(nums):
			print(slow, fast, sum, min_subarray)
			if sum < target:
				sum += nums[fast]
				fast += 1

			else:
				min_subarray = min(fast - slow, min_subarray)

				if min_subarray == 1:
					return 1

				sum -= nums[slow]
				slow += 1
		
		return min_subarray