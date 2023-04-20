# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
	def longestCommonPrefix(self, strs):
		if not strs:
			return ''

		shortest_string = min(strs, key = len)

		for index, character in enumerate(shortest_string):
			for string in strs:
				if string[index] != character:
					return shortest_string[:index]

		return shortest_string
