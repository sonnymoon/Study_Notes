# https://leetcode.com/problems/height-checker/
# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

# Time: O(n), Space: O(n)
class Solution(object):
	def heightChecker(self, heights):
		frequency = {}

		for height in heights:
			frequency[height] = frequency.get(height, 0) + 1

		differences = 0
		height_f = 1

		for height_h in heights:
			while not frequency.get(height_f):
				height_f += 1
			
			if height_h != height_f:
				differences += 1
			
			frequency[height_f] -= 1

		return differences

# Explanation
# The hash map "frequency" is used to track the frequency of the numbers in the array
# The variable "differences" is used to track the count of numbers that are different from the expected number at that index
# The variable "height_f" is used to track the numbers in "frequency"
# Each number "height_h" in the array is iterated through using a for loop
	# A nested while loop iterates "height_f" until it reaches a number with a frequency greater than 0
	# If "height_h" is not equal to "height_f", "differences" is incremented
	# The frequency of "height_f" is decremented
# When the for loop completes, the function returns "differences"