import io
from typing import List
class DSU:
    def __init__(self,n):
        self.rank = [0]*n
        self.parent = [i for i in range(0,n)]
        self.count_unions = 0
    def find_parent(self,n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find_parent(self.parent[n])
        return self.parent[n]
    def union(self,v1,v2):
        p1 = self.find_parent(v1)
        p2 = self.find_parent(v2)
        if p1 != p2:
            self.count_unions += 1
            r1 = self.rank[p1]
            r2 = self.rank[p2]
            if r1 > r2:
                self.parent[p2] = p1
            elif r2 > r1:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges_needed = 0
        edges.sort(reverse=True)
        dsu_alice = DSU(n)
        dsu_bob = DSU(n)

        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1
        
        ind = 0
        
        while (dsu_alice.count_unions != n-1 or dsu_bob.count_unions != n-1) and ind!= len(edges) and edges[ind][0] == 3:
            u = edges[ind][1]
            v = edges[ind][2]
            if dsu_bob.find_parent(u) != dsu_bob.find_parent(v):
                dsu_bob.union(u,v)
                dsu_alice.union(u,v)
                edges_needed += 1
            ind += 1

        while dsu_bob.count_unions != n-1 and ind!= len(edges) and edges[ind][0] == 2:
            u = edges[ind][1]
            v = edges[ind][2]
            if dsu_bob.find_parent(u) != dsu_bob.find_parent(v):
                dsu_bob.union(u,v)
                edges_needed += 1
            ind += 1
        
        while dsu_alice.count_unions != n-1 and ind!= len(edges):
            u = edges[ind][1]
            v = edges[ind][2]
            if dsu_alice.find_parent(u) != dsu_alice.find_parent(v):
                dsu_alice.union(u,v)
                edges_needed += 1
            ind += 1
        
        if dsu_alice.count_unions == n-1 and dsu_bob.count_unions == n - 1:
            return len(edges)-edges_needed
        else:
            return -1

obj = Solution()
#data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
#data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])
data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]])
print(data)