# https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Given an array arr of integers, check if there exist two indices i and j such that :
	# i != j
	# 0 <= i, j < arr.length
	# arr[i] == 2 * arr[j]

# Time: O(n), Space: O(n)
class Solution(object):
	def checkIfExist(self, arr):
		seen = set()

		for num in arr:
			if num * 2 in seen:
				return True

			if num % 2 == 0:
				if num / 2 in seen:
					return True

			seen.add(num)

		return False

# Explanation
# A hash set is implemented to keep track of the numbers that have already been read in the array
# The array is iterated through to see if the double of the number or the half of the number (if it is even) has already been seen
# As soon as a match is found, the function returns "True"
