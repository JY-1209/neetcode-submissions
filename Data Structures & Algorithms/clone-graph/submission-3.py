"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}

        def dfs(cur):
            if cur in clones:
                return clones[cur]
            
            copy_node = Node(cur.val, [])
            clones[cur] = copy_node

            for neighbor in cur.neighbors:
                copy_node.neighbors.append(dfs(neighbor))

            return copy_node

        return dfs(node)