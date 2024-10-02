# Python Program to Insert a Node At a Specific
# Position in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, position, data):
    new_node = Node(data)

    # If inserting at the beginning
    if position == 1:
        new_node.next = head
        head = new_node
        return head

    current = head
    for _ in range(1, position - 1):
        if current is None:
            break
        current = current.next

    # If the position is out of bounds
    if current is None:
        print("Position is out of bounds.")
        return head

    new_node.next = current.next
    current.next = new_node
    return head

def print_list(head):
    while head:
        print(f" {head.data}", end="")
        head = head.next
    print()

# Creating the list 3->5->8->10
head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(10)

data, pos = 12, 2
head = insert_at_position(head, pos, data)
print_list(head)
