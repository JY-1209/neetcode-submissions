"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        visited = {}

        def create_copy(node: 'Optional[Node]'):
            if not node:
                return None
            
            if node in visited:
                return visited[node]
            
            copy_node = Node(node.val)
            visited[node] = copy_node

            copy_node.next = create_copy(node.next)
            copy_node.random = create_copy(node.random)

            return copy_node
        
        return create_copy(head)
