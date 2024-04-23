import io
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<2:
            return [0]
        adj=[set() for _ in range(n)]
        for src,dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        leaves=[node for node in range(n) if len(adj[node])==1]
        while n>2:
            n-=len(leaves)
            leavesNext=[]
            for leaf in leaves:
                neb=adj[leaf].pop()
                adj[neb].remove(leaf)
                if len(adj[neb])==1:
                    leavesNext.append(neb)
            leaves=leavesNext
        return leaves

obj = Solution()
#data = obj.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]])
data = obj.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]])
print(data)