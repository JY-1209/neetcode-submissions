class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(cur):
            nonlocal res

            if not cur:
                return 0

            left = max(0, dfs(cur.left))
            right = max(0, dfs(cur.right))

            res = max(res, cur.val + left + right)

            return cur.val + max(left, right)

        dfs(root)
        return res