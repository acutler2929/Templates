#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a doubly linked list
# -------------------------------------------------------------------------------------------------
#  Notice that traversing B does not show A. To do so, we only need to add another reference to
# each node that references the previous node.

class Node:
    """Node for Doubly Linked List"""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev  # Reference to the previous item in the list
        self.next = next  # Reference to the next item in the list

    # Class method version
    def traverse(self, traversed=None):
        """Print out nodes"""
        traversed = traversed or []  # Empty list by default
        if self in traversed:
            return  # Already done
        traversed.append(self)
        # Do previous nodes
        if self.prev:
            self.prev.traverse(traversed=traversed)
        else:
            print('NULL -> ', end='')
        print("{} -> ".format(self.data), end='')
        # Do next nodes
        if self.next:
            self.next.traverse(traversed=traversed)
        else:
            print('NULL')  # Adds newline

# Recursive function version


def traverse_linked_list(node, traversed=None):
    """Print out nodes recursively"""
    traversed = traversed or []  # Empty list by default
    if not node or node in traversed:  # Another Base Case
        return
    traversed.append(node)
    # Do previous nodes
    if node.prev:
        traverse_linked_list(node.prev, traversed=traversed)
    else:
        print('NULL -> ', end='')
    print("{} -> ".format(node.data), end='')  # Set end='' to not do newline
    # Do next node
    if node.next:
        traverse_linked_list(node.next, traversed=traversed)
    else:
        print("NULL")


# Create Items
node_a = Node('A')
node_b = Node('B', prev=node_a)
node_c = Node('C', prev=node_b)
# Link up Items
node_a.next = node_b
node_b.next = node_c

# Start at A and show list
traverse_linked_list(node_a)  # NULL -> A -> B -> C -> NULL
node_a.traverse()  # NULL -> A -> B -> C -> NULL
# Start at B and show list
# Notice A _is_ referenced here
traverse_linked_list(node_b)  # NULL -> A -> B -> C -> NULL
node_b.traverse()  # NULL -> A -> B -> C -> NULL

# Traversing is more complicated if you want to start from any node but still print out the same traversal.
# The traversal function and method here makes use of a list to keep track of which nodes have already
# been traversed to not print out items multiple times.

# The classes above require you to manually link up nodes to form your linked list. As an ungraded exercise,
# see if you can add functions or methods to maintain your own linked list. Here is some example usage
# of such a class:

# linked = DoublyLinkedList()
# node_b = linked.append('B') # B
# node_a = linked.prepend('A') # A -> B
# node_c = linked.append('C') # A -> B -> C
# node_b.traverse() # A -> B -> C
