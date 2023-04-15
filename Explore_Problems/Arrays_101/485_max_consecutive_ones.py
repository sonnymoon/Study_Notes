# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Time: O(n), Space: O(1)
class Solution:
	def findMaxConsecutiveOnes(self, nums):
		count = max_count = 0

		for num in nums:
			if num == 1:
				count += 1
			else:
				max_count = max(count, max_count)
				count = 0

		return max(count, max_count)

# Explanation
# The variable "count" is used to track the number of consecutive 1's in the array
# The variable "max_count" is used to track the highest value of "count"
# Each number in the array is iterated through using a for loop
	# If the number is 1, "count" is incremented
	# Otherwise, the higher value between "count" and "max_count" is set to "max_count" and "count" is reset to 0
# After the iterations, the higher value between "count" and "max_count" is returned
