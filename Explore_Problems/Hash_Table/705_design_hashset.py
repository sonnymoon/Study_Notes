# https://leetcode.com/problems/design-hashset/
# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
	# void add(key) Inserts the value key into the HashSet.
	# bool contains(key) Returns whether the value key exists in the HashSet or not.
	# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet(object):
	def __init__(self, size = 1000000):
		self.size = size
		self.hash_set = [ None ] * self.size

	def add(self, key):
		self.hash_set[key % self.size] = key

	def remove(self, key):
		self.hash_set[key % self.size] = None

	def contains(self, key):
		return self.hash_set[key % self.size] == key
