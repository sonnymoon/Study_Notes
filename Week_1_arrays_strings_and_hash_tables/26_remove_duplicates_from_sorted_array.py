# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:
	# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
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
# The variable "write" is used to track the index at which a non-duplicate number should be written into "nums"
# The first number in the array is by definition a non-duplicate so "write" is instantiated at 1
# The array is iterated through starting from the second number to check if the number is the same as the number as the previous index
	# If the number is a duplicate, the number is ignored and "write" is not incremented
	# Otherwise, the number is written at the "write" index and "write" is incremented
# "write", which at this point is also the count of non-duplicate numbers, is returned
