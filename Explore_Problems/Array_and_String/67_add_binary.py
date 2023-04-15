# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
	def addBinary(self, a, b):
		read1 = len(a) - 1
		read2 = len(b) - 1

		carry = 0

		result = ""

		while read1 >= 0 or read2 >= 0:
			sum = carry

			if read1 >= 0 and a[read1] == '1':
				sum += 1

			if read2 >= 0 and b[read2] == '1':
				sum += 1

			read1 -= 1
			read2 -= 1

			if sum > 1:
				carry = 1
			else:
				carry = 0
			
			if sum % 2 == 0:
				result = '0' + result
			else:
				result = '1' + result
			
		if carry:
			result = '1' + result

		return result
