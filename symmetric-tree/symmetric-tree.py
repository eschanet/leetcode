# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def left_right_symmetric(left: TreeNode, right: TreeNode) -> bool:
            
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return (left.val == right.val) and left_right_symmetric(left.left, right.right) and left_right_symmetric(left.right, right.left)

        return left_right_symmetric(root.left, root.right)
        