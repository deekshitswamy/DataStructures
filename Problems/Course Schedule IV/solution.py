import io
from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pass

obj = Solution()
#data = obj.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])
#data = obj.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])
data = obj.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
print(data)