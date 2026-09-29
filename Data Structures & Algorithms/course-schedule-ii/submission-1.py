class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()
        stack = []

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
            stack.append(node)

            return False

        for node in graph:
            if cycles(node):
                return []

        return stack




        


