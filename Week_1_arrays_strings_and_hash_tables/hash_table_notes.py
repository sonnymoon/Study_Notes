# https://leetcode.com/explore/learn/card/hash-table/

# A hash table is a data structure that uses hash functions to store data

# Hash functions are used to store keys in buckets
# The goal for hash function design is to assign keys to buckets as uniformly as possible
	# In an ideal case, keys will be mapped one-to-one with buckets

# O(n)
def ideal_hash_function(buckets):
	data = [
		i
		for i in range(5)
	]

	for entry in data:
		buckets[entry % len(buckets.keys())].append(entry)

# Collisions occur when more than one key is mapped to the same bucket
	# If the capacity of a bucket is small, then a simple array could store the keys in a bucket
	# Otherwise, another data structure, like a binary tree, may be more applicable

# O(n)
def collision_hash_function(buckets):
	data = [
		i
		for i in range(7)
	]

	for entry in data:
		buckets[entry % len(buckets.keys())].append(entry)

def hash_table_testing():
	buckets = {
		0: [],
		1: [],
		2: [],
		3: [],
		4: []
	}

	print('BEFORE', buckets)

	# ideal_hash_function(buckets)

	# collision_hash_function(buckets)

	print('AFTER', buckets)

# Given m number keys that need to be hashed, the space complexity of a hash table is O(m)
# However, the time complexity is dependent on the design of the hash table
	# If bucket sizes are small enough, the time complexity for operations trend towards O(1)
	# If the bucket sizes are large, the time complexity for operations that of the data structure used for bucket design (O(n) for arrays, O(logn) for binary trees)

# There are two types of hash tables: hash sets and hash maps

# Hash sets are an implementation of sets, which are a data structure that stores elements that do not repeat

# Hash maps are an implementation of maps, which are a data structure that stores data in key and value pairs
# When more information is needed for a task, hash maps can be used to map the key to said information
	# The solution to a problem may just be a stored value for a key, a result achieved through decision making using the values, or an aggregate of the values
# Effective problem solving with hash maps requires an optimal strategy for designing the keys that will be used
	# All values that should be grouped together should be mapped to the same value in a hash map
	# Values that should not be grouped together should not be mapped to the same value in a hash map
	# Hash map key-to-value mappings differ from hash function key-to-bucket mappings in that multiple unlike keys may map to the same bucket for the latter
	# The keys may be just each of the data points themselves or some sort of modification to a key or multuple keys
		# Elements in an array vs elements that have been modified by some operation
		# Nodes of a tree vs serialization of a subtree
		# Index of one dimension of a multi-dimensional array vs. combination of the indexes of all the dimensions

