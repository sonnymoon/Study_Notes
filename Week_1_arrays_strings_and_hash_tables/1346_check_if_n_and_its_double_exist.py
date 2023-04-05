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
# The hash set "seen" is used to keep track of the numbers that have already been seen in the array
# Each number in the array is iterated through using a for loop
	# If the double of the number or the half of the number (if the number is even) has already been seen, the function returns "True"
	# If a match has not been found, the number is added to "seen" and the for loop continues
# If the for loop completes without returning "True, the function returns "False"
