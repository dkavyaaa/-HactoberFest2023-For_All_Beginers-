# Python3 implementation for the above approach.

import math

# Define a class for a node in the tree
class Node:
	def __init__(self, value=0):
		self.left = None
		self.right = None
		self.parent = None
		self.value = value

# Define a class for the ScapeGoat Tree
class SGTree:
	def __init__(self):
		self.root = None
		self.n = 0
		
	# Traverse the tree in preorder and print the node values
	def preorder(self, node):
		if node is not None:
			print(node.value, end=" ")
			self.preorder(node.left)
			self.preorder(node.right)
	
	# Get the size of the subtree rooted at a given node
	def size(self, node):
		if node is None:
			return 0
		return 1 + self.size(node.left) + self.size(node.right)
	
	# Insert a new node into the tree
	def insert(self, x):
		
		node = Node(x)
		
		# insert the node into the tree and get its depth
		h = self.BSTInsertAndFindDepth(node)
		
		# check if the tree is unbalanced
		if h > math.ceil(2.4663034623764317 * math.log(self.n, 3)):
			p = node.parent
			
			# find the root of the subtree to be rebuilt
			while 3*self.size(p) <= 2*self.size(p.parent):
				p = p.parent
			self.rebuildTree(p.parent) # rebuild the subtree
			
		return h >= 0
	
	def rebuildTree(self, u):

		# find the number of nodes in the subtree rooted at u
		n = self.size(u)

		# get u's parent
		p = u.parent

		# create an array of size n
		a = [None]*n

		# fill the array with nodes from the subtree rooted at u
		self.storeInArray(u, a, 0)

		if p is None:
			# if u is the root of the tree, build a balanced tree from the array
			self.root = self.buildBalancedFromArray(a, 0, n)
			self.root.parent = None

		elif p.right == u:
			# if u is the right child of its parent, build a balanced tree from the array
			# and make it the new right child of p
			p.right = self.buildBalancedFromArray(a, 0, n)
			p.right.parent = p

		else:
			# if u is the left child of its parent, build a balanced tree from the array
			# and make it the new left child of p
			p.left = self.buildBalancedFromArray(a, 0, n)
			p.left.parent = p

	def buildBalancedFromArray(self, a, i, n):

		# base case: if n is 0, return None
		if n == 0:
			return None

		# find the middle element of the array
		m = n // 2

		# create a node for the middle element and recursively build balanced
		# binary search trees from the left and right halves of the array
		a[i+m].left = self.buildBalancedFromArray(a, i, m)

		if a[i+m].left is not None:
			a[i+m].left.parent = a[i+m]
		a[i+m].right = self.buildBalancedFromArray(a, i+m+1, n-m-1)

		if a[i+m].right is not None:
			a[i+m].right.parent = a[i+m]

		# return the root of the balanced binary search tree
		return a[i+m]

	
	def BSTInsertAndFindDepth(self, u):
		w = self.root
		if w is None:
			self.root = u
			self.n += 1
			return 0
		done = False
		d = 0
		while not done:
			if u.value < w.value:
				if w.left is None:
					w.left = u
					u.parent = w
					done = True
				else:
					w = w.left
			elif u.value > w.value:
				if w.right is None:
					w.right = u
					u.parent = w
					done = True
				else:
					w = w.right
			else:
				return -1
			d += 1
		self.n += 1
		return d

# Main function for driver code
def main():
	
# Inserting elements into the tree
sgt = SGTree()
sgt.insert(7)
sgt.insert(6)
sgt.insert(3)
sgt.insert(1)
sgt.insert(0)
sgt.insert(8)
sgt.insert(9)
sgt.insert(4)
sgt.insert(5)
sgt.insert(2)
sgt.insert(3.5)
	
# Printing the preorder
print("Preorder traversal of the constructed ScapeGoat tree is:")
sgt.preorder(sgt.root)


if __name__=='__main__':
main()
	
