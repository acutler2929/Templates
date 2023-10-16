#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a singly linked list
# -------------------------------------------------------------------------------------------------
#  A linked list where each item refers to the next item only is called a Singly Linked List.
# Each item has only a single link. If you have a reference to the last item, we won't be able
# to access any other items since it doesn't have a reference backwards. Later we will cover
# doubly linked lists that will let you traverse forwards and backwards.

# Here's a simple python class that provides a simple singly linked list. It uses the term Node
# to refer to each item in the linked list.

class Node:
    """Node for Singly Linked List"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # Reference to the next item in the list

    # Class method version
    def traverse(self):
        """Print out nodes"""
        print("{} -> ".format(self.data), end='')  # Set end='' to not do newline
        # Do next node
        if self.next:
            self.next.traverse()
        else:
            print('NULL')  # Adds newline

# Recursive function version


def traverse_linked_list(node):
    """Print out nodes recursively"""
    if not node:  # Base Case
        print('NULL')  # Adds newline
        return
    print("{} -> ".format(node.data), end='')  # Set end='' to not do newline
    # Do next node
    traverse_linked_list(node.next)


# Create Items
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
# Link up Items
node_a.next = node_b
node_b.next = node_c

# Start at A and show list
traverse_linked_list(node_a)  # A -> B -> C -> NULL
node_a.traverse()  # A -> B -> C -> NULL
# Start at B and show list
# Notice A is not referenced at all here
traverse_linked_list(node_b)  # B -> C -> NULL
node_b.traverse()  # B -> C -> NULL
