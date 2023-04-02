# https://leetcode.com/problems/duplicate-zeros/
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Time: O(n), Space: O(1)
class Solution(object):
	def duplicateZeros(self, arr):
		arr_length = len(arr)

		zero_count = 0

		for i in range(arr_length):
			if arr[i] == 0:
				zero_count += 1

		for i in range(arr_length -1, -1, -1):
			print(I + zero_count)
			if i + zero_count < arr_length:
				arr[i + zero_count] = arr[i]
			
			if arr[i] == 0: 
				zero_count -= 1
				if i + zero_count < arr_length:
					arr[i + zero_count] = 0
