# https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
	def isPalindrome(self, head):
		slow = fast = head
		previous = None

		while slow is not None:
			forward_next = slow.next

			if fast is not None and fast.next is not None:
				fast = fast.next.next

			elif previous is None:
				previous = slow
				previous.next = None

			else:
				slow.next = previous
				previous = slow

			slow = forward_next

		left = head
		right = previous

		while right is not None:
			if left.val != right.val:
				return False
			
			left = left.next
			right = right.next
		
		return True
