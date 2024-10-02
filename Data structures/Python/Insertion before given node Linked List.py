# Python Implementation to insert a node before
# a given key using iteratinon
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Iterative function to insert a new node with value 
# newData before the node with the given key
def insert_before_key(head, key, newData):

    # Special case: if the key is at the head
    if head is None:
        return None

    # If the head's data matches the key, create 
    # and insert new node as the new head
    if head.data == key:
        new_node = Node(newData)
        new_node.next = head
        return new_node

    # Initialize pointers
    prev = None
    curr = head

    # Traverse the list to find the key
    while curr is not None and curr.data != key:
        prev = curr
        curr = curr.next

    # If the key was found
    if curr is not None:
        new_node = Node(newData)
        prev.next = new_node
        new_node.next = curr

    return head

def print_list(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list: 
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    newData = 6
    key = 2

    head = insert_before_key(head, key, newData)

    print_list(head)