# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxPath = -math.inf
        
        def path(root: TreeNode) -> int:
            if not root:
                return 0

            left = path(root.left)
            right = path(root.right)
            
            self.maxPath = max(self.maxPath, left + right + root.val)
            
            return max(left + root.val, right + root.val, 0)
            
        path(root)
        
        return self.maxPath