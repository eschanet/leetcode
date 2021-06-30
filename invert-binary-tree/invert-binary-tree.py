# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree_recursive(self, root: TreeNode) -> TreeNode:
        if root:            
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def invertTree_iterative(self, root: TreeNode) -> TreeNode:
        queue = [root]

        while len(queue) > 0:
            current = queue.pop()
            if not current: 
                break
            current.left, current.right = current.right, current.left
            
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        
        return root
        
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        # return self.invertTree_recursive(root)
        return self.invertTree_iterative(root)