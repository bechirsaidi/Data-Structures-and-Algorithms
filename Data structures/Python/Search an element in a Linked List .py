# Iterative Python program to search
# an element in linked list

# A Linked List Node
class Node:
  
      # Constructor to intialize a node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Checks whether key is present in linked list
def search_key(head, key):
  
    # Initialize curr with the head of linked list
    curr = head

    # Iterate over all the nodes
    while curr is not None:

        # If the current node's value is equal to key,
        # return true
        if curr.data == key:
            return True

        # Move to the next node
        curr = curr.next

    # If there is no node with value as key, return false
    return False

# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 14 -> 21 -> 13 -> 30 -> 10
    head = Node(14)
    head.next = Node(21)
    head.next.next = Node(13)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(10)

    # Key to search in the linked list
    key = 14

    if search_key(head, key):
        print("Yes")
    else:
        print("No")
