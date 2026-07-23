# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(root2, subRoot2):
            if not root2 and not subRoot2:
                return True
            if not root2:
                return False
            if not subRoot2:
                return False
            
            return dfs(root2.left, subRoot2.left) and dfs(root2.right, subRoot2.right) and root2.val == subRoot2.val

        isSubTree = dfs(root, subRoot)

        return isSubTree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)