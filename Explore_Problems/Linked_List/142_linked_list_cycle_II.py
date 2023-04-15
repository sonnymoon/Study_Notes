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
		if head is None:
			return None

		slow = head
		fast = head
		fast_index = 0
		cycle = False
		min_fast_index_post_cycle = None

		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				cycle = True


		return None