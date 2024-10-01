# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None
    
    # A dictionary to save the cloned nodes.
    clone_map = {}

    def dfs(n):
        # If the node is already cloned, return it.
        if n in clone_map:
            return clone_map[n]
        
        # Clone the node.
        clone_node = Node(n.val)
        clone_map[n] = clone_node
        
        # Iterate through the neighbors and clone them.
        for neighbor in n.neighbors:
            clone_node.neighbors.append(dfs(neighbor))
        
        return clone_node

    return dfs(node)

# Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
# Each node and each edge is processed once.

# Space Complexity: O(V), for the clone_map that stores the cloned nodes and the recursion stack.
