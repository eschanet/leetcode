# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        def is_symmetric_recursive(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return (left.val == right.val) and left_right_symmetric(left.left, right.right) and left_right_symmetric(left.right, right.left)
        
        def is_symmetric_iterative(left: TreeNode, right: TreeNode) -> bool:
            queue = [left, right]
            
            while len(queue) > 0:
                left = queue.pop()
                right = queue.pop()
                
                if not left and not right:
                    continue  
                elif not left or not right:
                    return False
                elif left.val != right.val:
                    return False
                
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
            
            return True
                
        # return is_symmetric_recursive(root.left, root.right)
        return is_symmetric_iterative(root.left, root.right)
        