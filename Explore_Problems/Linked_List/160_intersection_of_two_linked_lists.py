# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

class Solution:
	def getIntersectionNode(self, headA, headB):
		length_A = 1
		length_B = 1

		current_A = headA
		current_B = headB

		while current_A.next or current_B.next:
			if current_A.next:
				length_A += 1
				current_A = current_A.next
			
			if current_B.next:
				length_B += 1
				current_B = current_B.next

		current_A = headA
		current_B = headB

		if length_A == length_B == 1 and current_A == current_B:
			return current_A

		if length_A >= length_B:
			for _ in range(length_A - length_B):
				current_A = current_A.next
		else:
			for _ in range(length_B - length_A):
				current_B = current_B.next
			
		while current_A and current_B:
			if current_A == current_B:
				return current_A

			current_A = current_A.next
			current_B = current_B.next

		return None