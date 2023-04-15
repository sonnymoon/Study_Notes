# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Time: O(n), Space: O(1)
class Solution(object):
	def findDisappearedNumbers(self, nums):	
		for num in nums:
			index = abs(num) - 1
			nums[index] = -abs(nums[index])
		
		return [ i + 1 for i in range(len(nums)) if nums[i] > 0 ]

# Explanation
# Each number in the array is iterated through using a for loop
	# A variable "index" is assigned to the absolute value of the number minus 1
		# The indexes of the array themselves are used to mark whether the number has been seen in the array
	# The number at "index" is reassigned to the negative absolute value of that number
# The function returns an array of all the indexes of the array plus 1 where the number at that index is positive
