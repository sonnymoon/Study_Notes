# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Time: O(n), Space: O(1)
class Solution(object):
	def findDisappearedNumbers(self, nums):	
		for num in nums:
			index = abs(num) - 1
			nums[index] = -abs(nums[index])
		
		return [ i + 1 for i in range(len(nums)) if nums[i] > 0 ]

