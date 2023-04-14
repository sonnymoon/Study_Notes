# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

class Solution(object):
	def minSubArrayLen(self, target, nums):
		sum = 0
		fast = 0
		slow = 0
		window = 10001

		while fast < len(nums):
			sum += nums[fast]
			fast += 1

			while sum >= target:
				window = min(window, fast - slow + 1)
				sum -= nums[slow]
				slow += 1


		return 0 if window == 10001 else window