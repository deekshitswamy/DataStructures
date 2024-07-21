import io
from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topo_sort(queue,res,adj_list,indegree):
            while queue:
                curr = queue.pop(0)
                res.append(curr)
                for i in adj_list[curr]:
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
            return res
        Row = topo_sort(queue1,[],adj_l_A,indegree_A)
        Col = topo_sort(queue2,[],adj_l_B,indegree_B)
        if len(Row)==k and len(Col)==k:
            grid = [[0 for i in range(k)] for j in range(k)]
            ind = {}
            for i in range(k):
                ind[Col[i]] = i
            for i in range(k):
                j = ind[Row[i]]
                grid[i][j] = Row[i]
            return grid
        return []

        def topo(a):
            res = []
            q = []
            graph = defaultdict(list)
            indegree = defaultdict(int)

            for i,j in a: 
                graph[i].append(j) 
                indegree[j] += 1
            
            for i in range(1,k+1): 
                if i not in indegree: q.append(i)

            while q: 
                node = q.pop(0)
                res.append(node) 
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0: 
                        q.append(nei)

            return res

        rowTopo = topo(rowConditions) 
        colTopo = topo(colConditions)

        if len(rowTopo) != k or len(colTopo) != k: return []

        pos = defaultdict(list) 

        for i in range(k): pos[rowTopo[i]].append(i) 
        for i in range(k): pos[colTopo[i]].append(i)
        
        res = [[0]*k for i in range(k)]

        for num,[row,col] in pos.items():
            res[row][col] = num
        return res

obj = Solution()
#data = obj.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]])
data = obj.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]])
print(data)