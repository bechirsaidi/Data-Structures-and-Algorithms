# Python Program to Insert a Node after a 
# Given Node in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a new node after a given node
def insertAfter(head, key, newData):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # if curr becomes None means, given key is
    # not found in linked list
    if curr is None:
        return head

    # Allocate new node by given data and point
    # the next of newNode to curr's next &
    # point current next to newNode
    newNode = Node(newData)
    newNode.next = curr.next
    curr.next = newNode
    return head

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
  
    # Create the linked list 2->3->5->6
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(6)

    key = 3
    newData = 4
    head = insertAfter(head, key, newData)

    printList(head)