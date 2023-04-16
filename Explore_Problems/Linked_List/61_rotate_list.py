# https://leetcode.com/problems/rotate-list/
# Given the head of a linked list, rotate the list to the right by k places.

class Solution:
	def rotateRight(self, head, k):
		if head is None or head.next is None or k == 0:
			return head
		
		length = 0
		current = head

		while current is not None:
			length += 1
			current = current.next

		k %= length

		if k == 0:
			return head

		slow = fast = head

		for _ in range(k):
			if fast.next is None:
				fast = head
			else:
				fast = fast.next

		while fast.next is not None:
			slow = slow.next
			fast = fast.next

		fast.next = head
		head = slow.next
		slow.next = None

		return head

class Solution:
	def rotateRight(self, head, k):
		if head is None or head.next is None or k == 0:
			return head
		
		length = 1
		tail = head

		while tail.next is not None:
			length += 1
			tail = tail.next

		k %= length

		if k == 0:
			return head

		tail.next = head

		for _ in range(length - k):
			tail = tail.next
		
		head = tail.next
		tail.next = None

		return head
