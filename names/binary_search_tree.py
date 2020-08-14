"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is less than "head" node otherwise moves on to elif
        if value < self.value:
            # if value is less, finds an a node with None
            if self.left is None:
                # creates a new node that points to previous node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # same as above
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checks if head node is the data we're looking for
        if self.value == target:
            return True
        # if data is greater than head node checks right
        # side of tree to see if value is there
        if target > self.value:
            # checks if there is any data on right side of tree
            # if not returns false
            if self.right is None:
                return False
            # if target value is there, returns true
            else:
                return self.right.contains(target)
        # same as above
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

#     def iterative_depth_first_for_each(self, fn):
#         # DFT: LIFO
#         # we'll use a stack
#         stack = []
#         stack.append(self)

#         # so long as our stack has nodes in it
#         # there's more nodes to traverse
#         while len(stack) > 0:
#             # pop the top node from the stack
#             current = stack.pop()

#             # add the current node's right child first
#             if current.right:
#                 stack.append(current.right)

#             # add the current node's left child
#             if current.left:
#                 stack.append(current.left)

#             # call the anonymous function
#             fn(current.value)

#     from collections import deque

#     def iterative_breadth_first_for_each(self, fn):
#         # BFT: FIFO
#         # we'll use a queue to facilitate the ordering
#         queue = deque()
#         queue.append(self)

#         # continue to traverse so long as there
#         while len(queue) > 0:
#             current = queue.popleft()

#             if current.left:
#                 queue.append(current.left)

#             if current.right:
#                 queue.append(current.right)

#             fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        # lowest number is always on the left
        # base case
        if self is None:
            return None
        # checks is there is left side to tree
        if self.left:
            # discovers data in order from left side
            self.left.in_order_print()

        # prints data in order
        print(self.value)

        # same as above
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return

        q = Queue()
        q.enqueue(node)

        while len(q) > 0:
            node = q.dequeue()
            print(node.value)

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def dft_print(self, node):
        if node is None:
            return
        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            node = stack.pop()

            print(node.value)

            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# # bst.bft_print()
# # bst.dft_print()

# print("elegant methods")
# print("pre order")
# # bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# # bst.post_order_dft()
