# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		length = len(s)

		if length <= 1:
			return length

		seen = {}
		
		start = end = 1
		max_substring_length = 0

		while end < length:
			if s[end] in seen:
				start = max(seen[s[end]] + 1, start)

			seen[s[end]] = end

			end += 1

			max_substring_length = max(end - start, max_substring_length)

		return max_substring_length
