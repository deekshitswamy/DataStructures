import io
from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        arr[0]=1
        for idx in range(1,n):
            arr[idx]=min(arr[idx-1]+1,arr[idx])
        return arr[-1]

obj = Solution()
#data = obj.maximumElementAfterDecrementingAndRearranging(arr = [2,2,1,2,1])
#data = obj.maximumElementAfterDecrementingAndRearranging(arr = [100,1,1000])
data = obj.maximumElementAfterDecrementingAndRearranging(arr = [1,2,3,4,5])
print(data)