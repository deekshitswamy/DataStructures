import io
from typing import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        vol = [[heightMap[i][j] for j in range(n)] for i in range(m)]

        upt, init = True, True

        while upt:
            upt = False
            for i in range(1, m - 1):
                for j in range(1, n -1):
                    val = max(heightMap[i][j], min(vol[i - 1][j], vol[i][j - 1]))
                    if init or vol[i][j] > val:
                        vol[i][j] = val
                        upt = True
            init = False
            for i in range(m - 2, 0, -1):
                for j in range(n - 2, 0, -1):
                    val = max(heightMap[i][j], min(vol[i + 1][j], vol[i][j + 1]))
                    if vol[i][j] > val:
                        vol[i][j] = val
                        upt = True
        res = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if vol[i][j] > heightMap[i][j]:
                    res += vol[i][j] - heightMap[i][j]
        
        return res

obj = Solution()
#data = obj.trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
data = obj.trapRainWater(heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
print(data)