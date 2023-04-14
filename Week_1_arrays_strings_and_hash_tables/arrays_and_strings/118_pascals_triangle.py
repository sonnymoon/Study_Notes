# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution(object):
	def generate(self, numRows):
		result = [ None ] * numRows

		for row in range(numRows):
			result[row] = [ 1 ] * (row + 1)
			for column in range(1, row + 1):
				if column != row:
					result[row][column] = result[row - 1][column - 1] + result[row - 1][column]

		return result
