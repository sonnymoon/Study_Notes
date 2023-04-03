# https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
	# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
	# Return k.

# Time: O(n), Space: O(1)
class Solution(object):
	def removeElement(self, nums, val):
		write = 0

		for num in nums:
			if num != val:
				nums[write] = num
				write += 1

		return write

# Explanation
# The variable "write" is used to track the index at which a non-duplicate number should be written into "nums"
# The array is iterated through to check each number
	# If the number is the same as "val", the number is ignored and "write" is not incremented
	# Otherwise, the number is written at the "write" index and "write" is incremented
# "write", which at this point is also the count of numbers different from "val", is returned
