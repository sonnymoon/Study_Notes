# https://leetcode.com/problems/valid-mountain-array/
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
	# arr.length >= 3
	# There exists some i with 0 < i < arr.length - 1 such that:
		# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
		# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Time: O(n), Space: O(1)
class Solution(object):
	def validMountainArray(self, arr):
		length = len(arr)

		left = 0
		right = length - 1

		while left < length - 1 and arr[left] < arr[left + 1]:
			left += 1

		while right > 0 and arr[right] < arr[right - 1]:
			right -= 1

		return 0 < left == right < length - 1
