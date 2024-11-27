import io
from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = [0] * n  # Initialize the adjacency count array with zeros
        
        # Increment the adjacency list for each edge's destination
        for edge in edges:
            adj[edge[1]] += 1
        
        counter = 0
        result = -1
        
        # Check for nodes with no incoming edges
        for i in range(n):
            if adj[i] == 0:
                counter += 1
                if counter > 1:
                    return -1
                if result == -1:
                    result = i
        
        return result

obj = Solution()
#data = obj.findChampion(n = 3, edges = [[0,1],[1,2]])
data = obj.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]])
print(data)