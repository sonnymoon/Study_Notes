# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Time: O(n), Space: O(1)
class Solution:
	def findMaxConsecutiveOnes(self, nums):
		count = max_count = 0

		for num in nums:
			if num == 1:
				count += 1

				if count > max_count:
					max_count = count
			else:
				count = 0

		return max_count

# Explanation
# "count" = count of consecutive 1's
# "max_count" = highest value of "count"
# for each number in the array:
	# if the number is 1:
		# increment "count"
		# if "count" is greater than "max_count":
			# set "max_count" to the value of "count"
	# else:
		# "count" is reset to 0
# return "max_count"
