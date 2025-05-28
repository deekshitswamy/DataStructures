import io
from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        f = defaultdict(int)
        s = defaultdict(int)
        def bfs(start, k, tree):
            visited = set()
            q = deque([(start, 0)])

            while q:
                node, dist = q.popleft()
                if node in visited:
                    continue
                if dist <= k:
                    visited.add(node)
                    for n in tree[node]:
                        q.append((n, dist + 1))

            return len(visited)
        


        for i in tree1:
            f[i] = (bfs(i, k, tree1))
        
        for j in tree2:
            s[j] = (bfs(j, k-1, tree2))
        
        mx = max(val for val in s.values())

        ans = [0] * len(f)
        for e in f:
            ans[e] = f[e] + mx
        return ans

obj = Solution()
#data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2)
data = obj.maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1)
print(data)