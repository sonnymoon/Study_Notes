# https://leetcode.com/problems/duplicate-zeros/
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.

# Time: O(n), Space: O(1)
class Solution(object):
	def duplicateZeros(self, arr):
		length = len(arr)

		read = length - 1

		zeroes = arr.count(0)

		while zeroes > 0:
			if read + zeroes < length:
				arr[read + zeroes] = arr[read]
			
			if arr[read] == 0:
				zeroes -= 0

				if read + zeroes < length:
					arr[read + zeroes] = 0
			
			read -= 1

# Explanation
# The variable "read" is used to track the indexes of the numbers in the array and is initialized at the last index
# The variable "zeroes" is initialized as the count of 0's in the array
# The numbers of the array are iterated through backwards using a while loop that depends on "zeroes" being greater than 0
	# A "zeroes" count of 0's will be duplicated so only numbers whose index "read" plus "zeroes" is less than the length will be written back into the array at the sum index
	# If the index requirement is met, the number at "read" is written at the sum index
	# If the number at "read" is a 0, "zeroes" is decremented and 0 is written at the new sum index
		# The 0's are duplicated through having the original 0 written with the first if statement and the duplicate 0 written with the second if statement
	# "read" is decremented at each iteration
