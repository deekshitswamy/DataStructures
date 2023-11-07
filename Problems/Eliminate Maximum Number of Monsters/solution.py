import io
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        time=[]
        for i in range(n):
            time.append((dist[i]/speed[i]))
        time.sort()
        for i in range(n):
            if i>=time[i]:
                i-=1
                break
        return i+1  

obj = Solution()
#data = obj.eliminateMaximum(dist = [1,3,4], speed = [1,1,1])
#data = obj.eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1])
data = obj.eliminateMaximum(dist = [3,2,4], speed = [5,3,2])
print(data)