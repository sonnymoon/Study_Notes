# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		
		# Brute force
		merged_nums = []

		nums1_index = 0

		while len(merged_nums) < len(nums1) + len(nums2):
