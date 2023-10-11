import io
from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start=sorted(flowers,key=lambda x:x[0])
        end=sorted(flowers,key=lambda x:x[1])
        ans=[]
        for man in people:
            i=bisect_left(end,man,key=lambda x:x[1])
            j=bisect_right(start,man,key=lambda x:x[0])
            ans.append(j-i)

        return ans

obj = Solution()
#data = obj.fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11])
data = obj.fullBloomFlowers(flowers = [[1,10],[3,3]], poeple = [3,3,2])
print(data)