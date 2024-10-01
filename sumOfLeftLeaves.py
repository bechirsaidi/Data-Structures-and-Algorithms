# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0

    left_sum = 0
    
    # Check if the left child is a leaf
    if root.left and not root.left.left and not root.left.right:
        left_sum += root.left.val
    
    # Recursively call for left and right subtrees
    left_sum += sumOfLeftLeaves(root.left)
    left_sum += sumOfLeftLeaves(root.right)

    return left_sum

# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# We visit each node once.

# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack.
