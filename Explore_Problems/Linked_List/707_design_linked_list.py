# https://leetcode.com/problems/design-linked-list/
# Design your implementation of the linked list.
# You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next.
# val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.
# Implement the MyLinkedList class:
	# MyLinkedList() Initializes the MyLinkedList object.
	# int get(int index) Get the value of the indexth node in the linked list.
		# If the index is invalid, return -1.
	# void addAtHead(int val) Add a node of value val before the first element of the linked list.
		# After the insertion, the new node will be the first node of the linked list.
	# void addAtTail(int val) Append a node of value val as the last element of the linked list.
	# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
		# If index equals the length of the linked list, the node will be appended to the end of the linked list.
		# If index is greater than the length, the node will not be inserted.
	# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class MyLinkedList:
	def __init__(self, value = None):
		if value is None:
			self.head = None
			self.tail = None
			self.length = 0
		else:
			initial_node = Node(value)
			self.head = initial_node
			self.tail = initial_node
			self.length = 1

	def get(self, index, return_type = 'value'):
		if index < 0 or index >= self.length:
			return -1
		
		current_node = self.head

		for _ in range(index):
			current_node = current_node.next

		if return_type == 'value':
			return current_node.value
		else:
			return current_node
		
	def addAtHead(self, val):
		new_node = Node(val)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node

		self.length += 1

	def addAtTail(self, val):
		new_node = Node(val)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1

	def addAtIndex(self, index, val):
		if index < 0 or index > self.length:
			return
		
		if index == 0:
			return self.addAtHead(val)
		
		if index == self.length:
			return self.addAtTail(val)
		
		new_node = Node(val)

		previous_node = self.get(index - 1, 'node')

		new_node.next = previous_node.next

		previous_node.next = new_node
		
		self.length += 1

	def deleteAtHead(self):
		current_node = self.head

		if self.length <= 1:
			self.head = None
			self.tail = None
			self.length = 0
			return
		
		self.head = self.head.next
		current_node.next = None
		self.length -= 1

	def deleteAtTail(self):
		current_node = self.head

		if self.length <= 1:
			self.head = None
			self.tail = None
			self.length = 0
			return

		previous_node = self.head
		
		while current_node.next:
			previous_node = current_node
			current_node = current_node.next

		self.tail = previous_node
		self.tail.next = None
		self.length -= 1

	def deleteAtIndex(self, index):
		if index < 0 or index >= self.length:
			return
		
		if index == 0:
			return self.deleteAtHead()
			
		if index == self.length - 1:
			return self.deleteAtTail()
		
		previous_node = self.get(index - 1, 'node')
		current_node = previous_node.next

		previous_node.next = current_node.next
		current_node.next = None
		self.length -= 1
