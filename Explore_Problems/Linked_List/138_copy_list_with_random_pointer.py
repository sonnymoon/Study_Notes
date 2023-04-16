# https://leetcode.com/problems/copy-list-with-random-pointer/
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list.
# The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
	# val: an integer representing Node.val
	# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

class Node:
	def __init__(self, x, next = None, random = None):
		self.val = int(x)
		self.next = next
		self.random = random

class Solution:
	def copyRandomList(self, head):
		if head is None:
			return None

		original_to_new_map = {}

		original = head
		new = new_head = Node(head.val)

		while original is not None:
			new.val = original.val

			if original.next is not None:
				new.next = Node(0)
			else:
				new.next = None

			new.random = original.random

			original_to_new_map[original] = new

			original = original.next
			new = new.next

		new = new_head

		while new is not None:
			if new.random is not None:
				new.random = original_to_new_map[new.random]

			new = new.next

		return new_head

class Solution:
	def copyRandomList(self, head):
		original_current = head
		original_next = None

		while original_current is not None:
			original_next = original_current.next

			new_copy = Node(original_current.val)

			original_current.next = new_copy
			new_copy.next = original_next

			original_current = original_next

		original_current = head

		while original_current is not None:
			if original_current.random is not None:
				original_current.next.random = original_current.random.next
			
			original_current = original_current.next.next

		new_pre_head = Node(0)

		original_current = head
		new_copy = None
		new_current = new_pre_head

		while original_current is not None:
			original_next = original_current.next.next

			new_copy = original_current.next
			new_current.next = new_copy
			new_current = new_copy

			original_current.next = original_next

			original_current = original_next

		return new_pre_head.next
