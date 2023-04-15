# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head, n):
		if n == 1 and head.next is None:
			return None

		pre_head = ListNode(0, head)

		slow = pre_head
		fast = head

		for _ in range(n):
			fast = fast.next
		
		while fast is not None:
			slow = slow.next
			fast = fast.next
		
		slow.next = slow.next.next

		return pre_head.next