import io
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        px=[ 0 for i in range(n+1)]
        for i in range(n):
            px[i+1]=px[i]^arr[i]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if  px[j]==px[i-1]:
                    ans+=j-i
        return ans

obj = Solution()
#data = obj.countTriplets(arr = [2,3,1,6,7])
data = obj.countTriplets(arr = [1,1,1,1,1])
print(data)