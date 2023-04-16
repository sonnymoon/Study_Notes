# https://leetcode.com/problems/linked-list-cycle-ii/
# Given the head of a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
# It is -1 if there is no cycle.
# Note that pos is not passed as a parameter.
# Do not modify the linked list.

class Solution:
	def detectCycle(self, head):
		if head is None or head.next is None:
			return None
		
		seen = set()

		current = head

		while current is not None:
			if current in seen:
				return current
			
			seen.add(current)

			current = current.next

		return None

class Solution:
	def detectCycle(self, head):
		if head is None or head.next is None:
			return None
		
		slow = fast = entry = head

		while fast.next is not None and fast.next.next is not None:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				while slow != entry:
					slow = slow.next
					entry = entry.next
				return entry
		
		return None
