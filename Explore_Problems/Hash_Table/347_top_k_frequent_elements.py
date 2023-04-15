# https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

class Solution(object):
	def topKFrequent(self, nums, k):
		frequencies = {}

		for num in nums:
			frequencies[num] = frequencies.get(num, 0) + 1

		sorted_nums = sorted(frequencies.keys(), reverse = True, key = lambda key: frequencies[key])

		return sorted_nums[0:k]
