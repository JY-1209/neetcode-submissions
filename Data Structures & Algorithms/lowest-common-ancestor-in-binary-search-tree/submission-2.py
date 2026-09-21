# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca, lca_node = float("inf"), None

        def dfs(root):
            nonlocal lca
            nonlocal lca_node

            if not root:
                return
            
            if root.val >= p.val and root.val <= q.val or root.val >= q.val and root.val <= p.val:
                if root.val < lca:
                    lca = root.val
                    lca_node = root
            else:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return lca_node