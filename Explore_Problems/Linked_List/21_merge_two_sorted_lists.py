# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1, list2):
		pre_head = ListNode()

		current_node = pre_head

		while list1 is not None and list2 is not None:
			if list1.val <= list2.val:
				current_node.next = list1
				list1 = list1.next
			else:
				current_node.next = list2
				list2 = list2.next

			current_node = current_node.next

		if list1 is None:
			current_node.next = list2
		
		if list2 is None:
			current_node.next = list1

		return pre_head.next
