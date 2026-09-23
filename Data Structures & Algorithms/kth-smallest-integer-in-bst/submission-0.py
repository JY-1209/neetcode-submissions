# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []

        cur_node = root
        def dfs(cur_node):
            if not cur_node:
                return
            
            dfs(cur_node.left)
            sorted_list.append(cur_node.val)
            dfs(cur_node.right)
        
        dfs(cur_node)
        return sorted_list[k-1]
