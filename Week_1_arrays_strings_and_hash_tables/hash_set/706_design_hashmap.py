# https://leetcode.com/problems/design-hashmap/
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
	# MyHashMap() initializes the object with an empty map.
	# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
	# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
	# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap(object):
	def __init__(self, size = 1000000):
		self.size = size
		self.hash_map = [ None ] * self.size
		
	def put(self, key, value):
		index = key % self.size

		if not self.hash_map[index]:
			self.hash_map[index] = []
		
		self.hash_map[index].append([ key, value ])

	def get(self, key):
		index = key % self.size

		if not self.hash_map[index]:
			return None

		for [ entry_key, entry_value ] in self.hash_map[index]:
			if entry_key == key:
				return entry_value
		
		return None

	def remove(self, key):
		self.hash_map[key % self.size] = -1
