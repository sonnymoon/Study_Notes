# https://leetcode.com/problems/duplicate-zeros/
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Time: O(n), Space: O(1)
class Solution(object):
	def duplicateZeros(self, arr):
		length = len(arr)

		zeroes = arr.count(0)

		for i in range(length -1, -1, -1):
			if i + zeroes < length:
				arr[i + zeroes] = arr[i]

			if arr[i] == 0:
				zeroes -= 1
				if i + zeroes < length:
					arr[i + zeroes] = 0

# Explanation
# 