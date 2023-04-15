# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
# This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
# These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list.
# Let curr be a node with a child list.
# The nodes in the child list should appear after curr and before curr.next in the flattened list.
# Return the head of the flattened list.
# The nodes in the list must have all of their child pointers set to null.

class Solution:
	def flatten(self, head):
		current_node = head
		level = 0
		branches = {}

		while current_node is not None:
			if current_node.child is not None:
				branches[level] = current_node.next
				current_node.next = current_node.child
				current_node.child.prev = current_node
				current_node.child = None
				level += 1

			if current_node.next is None:
				if level > 0:
					level -= 1

					while branches[level] is None and level > 0:
						level -= 1

					current_node.next = branches[level]

					if branches[level] is not None:
						branches[level].prev = current_node

			current_node = current_node.next

		return head

class Solution:
	def flatten(self, head):
		current = head

		while current is not None:
			if current.child is None:
				current = current.next
			else:
				branch = current.child

				while branch.next is not None:
					branch = branch.next
				
				branch.next = current.next

				if current.next is not None:
					current.next.prev = branch
				
				current.next = current.child
				current.child.prev = current
				current.child = None

		return head
