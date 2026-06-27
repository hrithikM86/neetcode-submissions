from collections import deque
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

        visited = {}
        

        def bfs(node):
            queue = deque([node])
            visited[node] = Node(node.val)

            while queue:
                curr = queue.popleft()
                
                for nbr in curr.neighbors:
                    if nbr not in visited:
                        visited[nbr] = Node(nbr.val)
                        queue.append(nbr)

                    visited[curr].neighbors.append(visited[nbr])

        bfs(node)
        return visited[node]


        