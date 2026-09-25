from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        visited = {}

        def bfs(node):
            queue = deque([node])
            visited[node] = Node(node.val)

            while queue:
                cur = queue.popleft()

                for child in cur.neighbors:
                    if child not in visited:
                        visited[child] = Node(child.val)
                        queue.append(child)
                    visited[cur].neighbors.append(visited[child])

        bfs(node)
        return visited[node]
