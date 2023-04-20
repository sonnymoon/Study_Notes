# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
	def strStr(self, haystack, needle):
		haystack_length = len(haystack)
		needle_length = len(needle)

		if haystack_length == 0:
			return -1
		
		if needle_length == 0:
			return 0

		if haystack_length < needle_length:
			return -1
		
		haystack_index = needle_index = 0

		for i in range(haystack_length - needle_length + 1):
			while haystack[haystack_index] == needle[needle_index]:
				haystack_index += 1
				needle_index += 1

				if needle_index == needle_length:
					return i
			
			haystack_index = i + 1
			needle_index = 0

		return -1
