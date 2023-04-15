# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def removeElements(self, head, val):
		if head is None:
			return None
		
		pre_head = ListNode(None, head)

		previous_node = pre_head
		current_node = head

		while current_node:
			if current_node.val == val:
				previous_node.next = None
			else:
				previous_node.next = current_node
				previous_node = current_node
	
			current_node = current_node.next

		return pre_head.next
