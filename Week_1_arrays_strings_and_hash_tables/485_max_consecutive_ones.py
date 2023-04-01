# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		overall_max = current_max = 0
		
		for i in range(len(nums)):
			if nums[i] == 1:
				current_max += 1
			else:
				if current_max > overall_max:
					overall_max = current_max
				current_max = 0

		if current_max > overall_max:
			overall_max = current_max  

		return overall_max