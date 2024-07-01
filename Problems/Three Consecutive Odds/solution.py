import io
from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n=len(arr)
        for i in range(n):
            if i+2<n and arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                return True
        return False

obj = Solution()
#data = obj.threeConsecutiveOdds(arr = [2,6,4,1])
data = obj.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12])
print(data)