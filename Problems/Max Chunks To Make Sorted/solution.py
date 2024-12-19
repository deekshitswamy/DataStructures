import io
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk = 0
        max_val = [0] * len(arr)
        max_val[0] = arr[0]

        for i in range(1, len(arr)):
            max_val[i] = max(max_val[i - 1], arr[i])

        for i in range(len(arr)):
            if max_val[i] == i:
                chunk += 1
        
        return chunk

obj = Solution()
#data = obj.maxChunksToSorted(arr = [4,3,2,1,0])
data = obj.maxChunksToSorted(arr = [1,0,2,3,4])
print(data)