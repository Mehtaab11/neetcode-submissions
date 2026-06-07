class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in output:
                return True

            cycle.add(crs)
            for nei in preMap[crs]:
                if dfs(nei) == False:
                    return False

            cycle.remove(crs)

            # visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return output
