# https://leetcode.com/problems/move-zeroes/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Time: O(n), Space: O(1)
class Solution(object):
	def moveZeroes(self, nums):
		length = len(nums)

		read = write = 0

		while write < length:
			if read < length:
				if nums[read] != 0:
					nums[write] = nums[read]
					write += 1

				read += 1
			else:
				nums[write] = 0
				write += 1

# Explanation
# The variable "read" is used to track the indexes of each number read while iterating through the array
# The variable "write" is used to track the indexes at which each non-zero number should be written in-place into the array
# The indexes of the array are iterated through using a while loop
	# The while loop continues until all indexes of the array have been written in to
	# If "read" is less than the length of the array, the number at "read" is checked to see if it is equal to 0
		# If the number at "read" is not 0, it is written into the array at index "write" and "write" is incremented
		# "read" is incremented
	# Otherwise, all the non-zero numbers have been read so 0's are writen in the remaining indexes of the array using "write"
