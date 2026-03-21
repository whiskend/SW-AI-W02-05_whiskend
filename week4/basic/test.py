# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
left_depth = 0
right_depth = 0
def preorder(root):
    
    if root is None:
        return
    
    preorder(root.left)
    left_depth += 1
    preorder(root.right)
    right_depth += 1

    return left_depth, right_depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left_depth, right_depth = preorder(root)
        depth = max(left_depth, right_depth)
        return depth
    