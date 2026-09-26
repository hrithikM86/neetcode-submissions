from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:  # Not connected
            return False

        def to_adj_list(edges):  # Convert to adj list
            adj_list = defaultdict(list)

            for i, j in edges:
                adj_list[i].append(j)
                adj_list[j].append(i)

            return adj_list

        visited = set()

        def cycles(adj_list, node, parent, visited):
            visited.add(node)

            for child in adj_list.get(node, []):
                if child not in visited:
                    if cycles(adj_list, child, node, visited):
                        return True
                elif child != parent:
                    return True

            return False

        adj_list = to_adj_list(edges)
        if cycles(adj_list, 0, None, visited):
            return False
        return len(visited) == n
