# https://leetcode.com/problems/merge-sorted-array/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.

# Time: O(m + n), Space: O(1).
class Solution(object):
	def merge(self, nums1, m, nums2, n):
		read1 = m - 1
		read2 = n - 1
		write = m + n - 1

		while read2 >= 0:
			if read1 >= 0 and nums1[read1] > nums2[read2]:
				nums1[write] = nums1[read1]
				read1 -= 1
			else:
				nums1[write] = nums2[read2]
				read2 -= 1
			write -= 1

# Explanation
# Two variables "read1" and "read2" are used to track the index of the numbers in "nums1" and "nums2", respectively
# The variable "write" is used to track the index at which a number should be written into "nums1"
# Instead of iterating through the numbers of either array, a while loop is used to 
