# https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1, l2):
		head = l1
		previous = None
		carry = 0

		while l1 is not None or l2 is not None:
			sum = l1.val + carry
			
			if l2 is not None:
				sum += l2.val
				l2 = l2.next
			
			if sum > 9:
				carry = 1
			else:
				carry = 0

			l1.val = sum % 10

			if l1.next is None:
				l1.next = l2
				l2 = None

			previous = l1
			l1 = l1.next

		if carry == 1:
			previous.next = ListNode(1)
		
		return head


class Solution:
	def addTwoNumbers(self, l1, l2):
		carry = 0
		pre_head = ListNode(0)
		current_node = pre_head

		while carry or l1 is not None or l2 is not None:
			sum = carry

			if l1 is not None:
				sum += l1.val
				l1 = l1.next
			
			if l2 is not None:
				sum += l2.val
				l2 = l2.next

			if sum > 9:
				carry = 1
			else:
				carry = 0

			current_node.next = ListNode(sum % 10)

			current_node = current_node.next

		return pre_head.next
