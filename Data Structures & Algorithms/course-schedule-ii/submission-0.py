class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()

        def cycles(node):
            if node in path:
                return True

            if node in visited:
                return False

            path.add(node)

            for child in graph.get(node, []):
                if cycles(child):
                    return True

            path.remove(node)
            visited.add(node)

            return False

        for node in graph:
            if cycles(node):
                return []

        checked = set()
        stack = []

        def topo(node):
            if node in checked:
                return

            checked.add(node)

            for child in graph.get(node,[]):
                topo(child)

            stack.append(node)

        for node in graph:
            topo(node)

        return stack

        


