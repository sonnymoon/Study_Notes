# https://leetcode.com/problems/diagonal-traverse/
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution(object):
	def findDiagonalOrder(self, mat):
		row_length = len(mat)
		column_length = len(mat[0])

		result = [ 0 ] * row_length * column_length

		row = 0
		column = 0
		write = 0
		direction = 1

		while row < row_length and column < column_length:
			result[write] = mat[row][column]
			write += 1

			if direction == 1:
				if column == column_length - 1:
					row += 1
					direction = -1
				elif row == 0:
					column += 1
					direction = -1
				else:
					row -= 1
					column += 1
			else:
				if row == row_length - 1:
					column += 1
					direction = 1
				elif column == 0:
					row += 1
					direction = 1
				else:
					row += 1
					column -= 1

		return result