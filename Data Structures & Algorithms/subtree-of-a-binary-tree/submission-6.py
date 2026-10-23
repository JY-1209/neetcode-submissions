# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return False
        if subRoot and not root:
            return False
        if not root and not subRoot:
            return True

        def isSameTree(node_a, node_b):
            if node_a and not node_b:
                return False
            if node_b and not node_a:
                return False
            if not node_a and not node_b:
                return True
            
            return node_a.val == node_b.val and isSameTree(node_a.left, node_b.left) and isSameTree(node_b.right, node_a.right)
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)