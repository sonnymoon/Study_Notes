# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:
	# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
	# The remaining elements of nums are not important as well as the size of nums.
	# Return k.

# Time: O(n), Space: O(1)
class Solution(object):
	def removeDuplicates(self, nums):
		write = 1

		for read in range(1, len(nums)):
			if nums[read] != nums[read - 1]:
				nums[write] = nums[read]
				write += 1

		return write

# Explanation
# The variable "write" is used to track the indexes at which non-duplicate numbers should be written in-place into the array
# Each index "read" is iterated through the array starting from 1 using a for loop
	# The first number in the array is by definition a non-duplicate number so "write" is initialized at 1 and "read" starts from 1
	# If the number is not the same as the previous number, the number is not a duplicate so it is written at the "write" index and "write" is incremented
# The function returns "write", which is also the count of non-duplicate numbers