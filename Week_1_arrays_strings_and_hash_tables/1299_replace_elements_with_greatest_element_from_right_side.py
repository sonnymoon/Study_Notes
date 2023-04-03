# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

# Time: O(n), Space: O(1)
class Solution(object):
	def replaceElements(self, arr):
		length = len(arr)

		previous = greatest = arr[length - 1]

		for i in range(length - 2, -1, -1):
			greatest = max(previous, greatest)
			previous = arr[i]
			arr[i] = greatest

		arr[length - 1] = -1

		return arr

# Explanation
# The variable "greatest" is used to track the greatest number on the right side of the current index
# The variable "previous" is used to track the number directly to the right of the current index
# Both "greatest" and "previous" are instatiated to the last number in the array
# The array is iterated through backwards starting from the second to last number to calculate "previous" and "greatest" at each index
	# "greatest" is the higher number between the current "greatest" and "previous"
	# "previous" is reassigned to the number at the current index so that it can be used in the next iteration
	# The number at the current index is then reassigned to the newly calculated "greatest"
# The last number is reassigned to -1 and the array is returned
