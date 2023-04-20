# https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
	# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	# int get(int key) Return the value of the key if the key exists, otherwise return -1.
	# void put(int key, int value) Update the value of the key if the key exists.
	# Otherwise, add the key-value pair to the cache.
	# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class LRUNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.length = 0
		self.head = None # least recently used
		self.tail = None # most recently used
		self.map = {}

	def move_to_tail(self, node):
		if self.length == 1 or node == self.tail:
			return

		if node == self.head:
			self.head = self.head.next
			self.head.prev = None
		else:
			node.prev.next = node.next
		
		if node.next is not None:
			node.next.prev = node.prev

		self.tail.next = node
		node.prev = self.tail
		node.next = None

		self.tail = node

	def get(self, key):
		print(f'GET [{key}]')

		if self.length == 0 or self.map.get(key, None) is None:
			return -1

		node = self.map[key]

		self.move_to_tail(node)

		if self.head is not None:
			print(self.head.next)
		else:
			print('self.head is None')
		
		if self.tail is not None:
			print(self.tail.prev)
		else:
			print('self.tail is None')

		return node.value

	def put(self, key, value):
		print(f'PUT [{key}, {value}]')

		if self.length == self.capacity:
			if self.map.get(key, None) is not None:
				node = self.map[key]
			else:
				node = self.head
			
			self.map[node.key] = None
			self.map[key] = node

			node.key = key
			node.value = value

			self.move_to_tail(node)

		else:
			if self.map.get(key, None) is not None:
				node = self.map[key]

				self.map[node.key] = None
				self.map[key] = node

				node.key = key
				node.value = value

				self.move_to_tail(node)
			else:
				node = LRUNode(key, value)

				if self.length == 0:
					self.head = node
				else:
					self.tail.next = node
					node.prev = self.tail
				
				self.tail = node
				self.map[key] = node
				self.length += 1

		if self.head is not None:
			print(self.head.next)
		else:
			print('self.head is None')
		
		if self.tail is not None:
			print(self.tail.prev)
		else:
			print('self.tail is None')

