# 문제링크: https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 종료 조건
        if root is None:
            return 0
        
        # 분리
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 합체
        return max(left_depth, right_depth) + 1