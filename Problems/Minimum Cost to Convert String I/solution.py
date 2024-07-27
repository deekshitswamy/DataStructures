import io
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize the graph with infinite costs
        graph = [[inf] * 26 for _ in range(26)]
        
        # Set the cost of a character to itself as 0
        for i in range(26):
            graph[i][i] = 0
        
        # Populate the graph with given transformation costs
        for o, c, cost in zip(original, changed, cost):
            x, y = ord(o) - ord('a'), ord(c) - ord('a')
            graph[x][y] = min(graph[x][y], cost)
        
        # Apply Floyd-Warshall algorithm to find shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        # Calculate the total cost of transformation
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                cost = graph[ord(s) - ord('a')][ord(t) - ord('a')]
                if cost == inf:
                    return -1  # Impossible to transform
                total_cost += cost
        
        return total_cost

obj = Solution()
#data = obj.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
#data = obj.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
data = obj.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000])
print(data)