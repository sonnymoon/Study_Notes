# https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
	def reverseList(self, head):
		if head is None or head.next is None:
			return head
		
		previous_node = None
		current_node = head
		next_node = head.next

		while current_node:
			next_node = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node

		return previous_node