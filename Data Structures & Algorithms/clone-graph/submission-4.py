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

        def dfs(node: Optional['Node']):
            if node in clones:
                return clones[node]

            copy_node = Node(node.val, [])
            clones[node] = copy_node

            for node_neighbor in node.neighbors:
                copy_neighbor_node = dfs(node_neighbor)
                copy_node.neighbors.append(copy_neighbor_node)
            
            return copy_node
        
        return dfs(node)