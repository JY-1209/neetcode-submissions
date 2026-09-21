# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_subtree_helper(root, sub_root):
            if root and not sub_root:
                return False

            if not root and sub_root:
                return False

            if not root and not sub_root:
                return True
            
            return root.val == sub_root.val and is_subtree_helper(root.left, sub_root.left) and is_subtree_helper(root.right, sub_root.right)
        
        def find_subtree(root):
            if not root and subRoot:
                return False
            
            if not root and not subRoot:
                return True
            
            return is_subtree_helper(root, subRoot) or find_subtree(root.left) or find_subtree(root.right)
        
        return find_subtree(root)