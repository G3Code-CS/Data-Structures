
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #  solution without recursion
        # current = self
        # traverse_nodes = True
        # while traverse_nodes:
        #     if current.value > value and current.left:
        #         current = current.left
        #     elif current.value <= value and current.right:
        #         current = current.right
        #     elif current.value > value and not current.left:
        #         current.left = BinarySearchTree(value)
        #         traverse_nodes = False
        #     elif current.value < value and not current.right:
        #         current.right = BinarySearchTree(value)
        #         traverse_nodes = False
        # check if new value is less than the current node
        if value < self.value:
            #is there already a value at self.left
            # If there is no self.left value set the new left child to be the value
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right=BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

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

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
