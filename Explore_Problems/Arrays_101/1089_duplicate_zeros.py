# https://leetcode.com/problems/duplicate-zeros/
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.

# Time: O(n), Space: O(1)
class Solution(object):
	def duplicateZeros(self, arr):
		length = len(arr)

		read = write = length - 1

		for num in arr:
			if num == 0:
				write += 1

		while write - read > 0:
			if write < length:
				arr[write] = arr[read]
			
			if arr[read] == 0:
				write -= 1

				if write < length:
					arr[write] = 0

			read -= 1
			write -= 1

# Explanation
# "length" = length of the array
# "read" = index of the current number in the array, starting at the last index
# "write" = index of the array to write into, starting at the last index
# iterate through the numbers of the array using a for loop
	# if the number is 0
		# increment "write"
# iterate while the difference between "write" and "read" is greater than 0 using a while loop
	# if "write" is less than "length"
		# set the number at "write" to the number at "read"
	# if the number at "read" is 0
		# decrement "write"
		# if "write" is less than "length"
			# set the number at "write" to 0
	# decrement "read" and "write"
