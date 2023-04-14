# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
	def strStr(self, haystack, needle):
		length1, length2 = len(haystack), len(needle)

		if length2 == 0:
			return 0
		
		if length2 > length1:
			return -1

		for read1 in range(length1 - length2 + 1):
			for read2 in range(length2):
				if haystack[read1 + read2] != needle[read2]:
					break

				if read2 == length2 - 1:
					return read1

		return -1

	def strStr(self, haystack, needle):
		length1, length2 = len(haystack), len(needle)

		if length2 == 0:
			return 0

		if length2 > length1:
			return -1
	
		failure = [ 0 ] * length2
		j = 0

		for i in range(1, length2):
			while j > 0 and needle[i] != needle[j]:
					j = failure[j-1]
			if needle[i] == needle[j]:
					j += 1
			failure[i] = j
		
		# Use the failure table to search for occurrences of the needle string in the haystack string
		j = 0
		for i in range(len(haystack)):
				while j > 0 and haystack[i] != needle[j]:
						j = failure[j-1]
				if haystack[i] == needle[j]:
						j += 1
				if j == len(needle):
						return i - len(needle) + 1
		
		return -1