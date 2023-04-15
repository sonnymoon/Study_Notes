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

		if left == 0:
			return False

		while right > 0 and arr[right] < arr[right - 1]:
			right -= 1

		return 0 < left == right < length - 1

# Explanation
# The variables "left" and "right" are used to track the indexes of the array from the left and right sides, respectively
# Each index is iterated through using a while loop
	# Each while loop continues while "left" and "right" have not reached the other end of the array and the next number is greater than the current number
	# After the first while loop, if "left" is still the same as its initialized index, the function returns "False"
# After the two while loops have completed, the function returns whether "left" and "right" are equal indexes and are not the first and last indexes of the array
