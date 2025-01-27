import io
from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        canTake = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            canTake[pre][course] = True

        for mid in range(numCourses):
            for src in range(numCourses):
                for dst in range(numCourses):
                    canTake[src][dst] = canTake[src][dst] or (canTake[src][mid] and canTake[mid][dst])
        
        return [canTake[u][v] for u, v in queries]

obj = Solution()
#data = obj.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])
#data = obj.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])
data = obj.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
print(data)