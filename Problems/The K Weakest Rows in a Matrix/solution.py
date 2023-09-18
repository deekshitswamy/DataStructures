import io
from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        n=len(mat)
        for i in range(n):
            ans.append([mat[i].count(1),i])

        ans.sort()    
        return [i[1] for i in ans[:k]]

obj = Solution()
#data = obj.kWeakestRows(mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3)
data = obj.kWeakestRows(mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], k = 2)
print(data)