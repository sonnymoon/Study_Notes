# https://leetcode.com/problems/odd-even-linked-list/
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class Solution:
	def oddEvenList(self, head):
		if head is not None:
			odd = head
			even = first_even = head.next

			while even is not None and even.next is not None:
				odd.next = odd.next.next
				even.next = even.next.next

				odd = odd.next
				even = even.next

			odd.next = first_even

		return head
