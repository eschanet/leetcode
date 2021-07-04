# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def same_tree_recursive(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        def same_tree_iterative(p: TreeNode, q: TreeNode) -> bool:
            from collections import deque

            def check(p, q):
                if not p and not q:
                    return True
                if not p or not q:
                    return False
                if p.val != q.val:
                    return False
                return True
        
            deq = deque([(p,q),])
            while deq:
                p, q = deq.popleft()
                if not check(p,q):
                    return False
                
                if p and q:
                    deq.append((p.left, q.left))
                    deq.append((p.right, q.right))
            
            return True
        
        # return same_tree_iterative(p, q)        
        return same_tree_recursive(p, q)