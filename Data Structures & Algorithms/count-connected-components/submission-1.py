class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = {i: [] for i in range(n)}
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        print(adj_list)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)

            for child in adj_list[node]:
                if child not in visited:
                    dfs(child)
            return 1
        
        for key, values in adj_list.items():
            count += dfs(key)

        return count



