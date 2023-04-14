# https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution(object):
	def spiralOrder(self, matrix):
		row_length = len(matrix)
		column_length = len(matrix[0])

		result = [ 0 ] * row_length * column_length

		row = 0
		column = 0
		write = 0
		direction = 0

		row_max = row_length - 1
		row_min = 1
		column_max = column_length - 1
		column_min = 0

		while write < row_length * column_length:
			result[write] = matrix[row][column]
			write += 1

			if direction % 4 == 0:
				if column == column_max:
					column_max -= 1
					direction += 1
					row += 1
				else:
					column += 1
			elif direction % 4 == 1:
				if row == row_max:
					row_max -= 1
					direction += 1
					column -= 1
				else:
					row += 1
			elif direction % 4 == 2:
				if column == column_min:
					column_min += 1
					direction += 1
					row -= 1
				else:
					column -= 1
			elif direction % 4 == 3:
				if row == row_min:
					row_min += 1
					direction += 1
					column += 1
				else:
					row -= 1
		
		return result