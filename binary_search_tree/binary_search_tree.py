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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # LEFT
        if value < self.value:
            # if there's no node on the left, stop here and make a new node
            if not self.left:
                self.left = BSTNode(value)
            else:
                # keep searching
                self.left.insert(value)
    
        # RIGHT
        else:
            # if there's no node on the right, stop here and make a new node
            if not self.right:
                self.right = BSTNode(value)
            else:
                # keep searching
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    
        # self is the starting point (root)
        # target is what we pass in to see if it's in the tree

        # return False if we know we need to go in one direction
        # but there's nothing in the left or right direction

        # once target is equal to our current node, we stop the recursion
        if target == self.value:
            return True

        # LEFT
        if target < self.value:
            # if we hit a dead end, that means the target isn't in the tree
            if not self.left:
                return False
            # if current node != target and there's still a left node, keep going
            return self.left.contains(target)

        # RIGHT
        else:
            # if there are no more right nodes, we hit a dead end and target isn't inside tree
            if not self.right:
                return False
            # if current node != target and there's still a right node, keep going
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # check the whole right branch until we're at the last leaf
        if not self.right:
            # return node we're on, this is what ends the recursion
            return self.value
        else:
            # keep er goin
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        # fn is going to be the function we pass in
        # call the fn on the value at this node
        fn(self.value)

        # pass function to the left and right children
        # recursion stops if self.left/right is None
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
