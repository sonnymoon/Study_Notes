

# A linked list is a collection of elements where each element references the next element in sequence
	# Like an array, a linked list is also a linear data structure
	# A linked list differs from an array in that the elements of a linked list are not contiguous in memory like the elements of an array
	# Additionally, the elements of a linked list do not have explicit indexes that can be used to reference them

# The elements of a linked list are called "nodes"

class LinkedListNode:
	# Each node is initialized with "value" and "next" attributes that track the value of the node and the reference to the next node, respectively
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	# A linked list can be initialized to be empty or with a single node whose value is the "value" attribute that is passed in
	# The first node is called the "head" and the last node is called the "tail"
	# Linked lists also keep track of its "length", which is the number of nodes it contains
	def __init__(self, value = None):
		if value is None:
			self.head = None
			self.tail = None
			self.length = 0
		else:
			initial_node = LinkedListNode(value)
			self.head = initial_node
			self.tail = initial_node
			self.length = 1
	
	def print(self):
		current_node = self.head

		while current_node:
			print(current_node.value)
			current_node = current_node.next

	# A new node can be appended to the end of a linked list by reassigning the tail reference to the new node
	# Time: O(1)
	def append(self, value):
		new_node = LinkedListNode(value)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1
		return True
	
	# The last node of a linked list can be popped by reassigning the tail reference to the second to last node
	# Time: O(n)
	def pop(self):
		current_node = self.head

		if self.length <= 1:
			self.head = None
			self.tail = None
			self.length = 0

			return current_node

		previous_node = self.head
		
		while current_node.next:
			previous_node = current_node
			current_node = current_node.next

		self.tail = previous_node
		self.tail.next = None
		self.length -= 1

		return current_node

	# A new node can be prepended to the start of a linked list by reassigning the head reference to the new node
	# Time: O(1)
	def prepend(self, value):
		new_node = LinkedListNode(value)

		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node

		self.length += 1
		return True
	
	# The first node of a linked list can be popped by reassigning the head reference to the second node
	# Time: O(1)
	def pop_first(self):
		current_node = self.head

		if self.length <= 1:
			self.head = None
			self.tail = None
			self.length = 0

			return current_node
		
		self.head = self.head.next
		current_node.next = None
		self.length -= 1

		return current_node
	
	# A node at any index can be accessed by iterating through the linked list
	# Time: O(n)
	def get(self, index):
		if index < 0 or index >= self.length:
			return None
		
		current_node = self.head

		for _ in range(index):
			current_node = current_node.next

		return current_node
	
	# A node at any index can have its value changed by accessing the node at that index and reassigning its value
	# Time: O(n)
	def set_value(self, index, value):
		current_node = self.get(index)

		if current_node:
			current_node.value = value
			return True
		
		return False
	
	# A node can be inserted at any index by accessing the node at the previous index and reassigning next references
	# Time: O(1) or O(n) depending on where the new node is being inserted
	def insert(self, index, value):
		if index < 0 or index > self.length:
			return False
		
		if index == 0:
			return self.prepend(value)
		
		if index == self.length:
			return self.append(value)
		
		new_node = LinkedListNode(value)

		previous_node = self.get(index - 1)

		new_node.next = previous_node.next

		previous_node.next = new_node
		
		self.length += 1

		return True
	
	# A node can be removed at any index by accessing the node at the previous index and reassigning next references
	# Time: O(1) or O(n) depending on where the node is being removed
	def remove(self, index):
		if index < 0 or index >= self.length:
			return None
		
		if index == 0:
			return self.pop_first()
		
		if index == self.length - 1:
			return self.pop()
		
		previous_node = self.get(index - 1)
		current_node = previous_node.next

		previous_node.next = current_node.next
		current_node.next = None
		self.length -= 1

		return current_node
	
	# A linked list can be reversed by flipping the head and tail references and iterating through the nodes to reassign next references to the previous node
	def reverse(self):
		current_node = self.head
		self.head = self.tail
		self.tail = current_node

		previous_node = None
		next_node = current_node.next

		for _ in range(self.length):
			next_node = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node
