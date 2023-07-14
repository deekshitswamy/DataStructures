import io
from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subseqs = {}
        for n in arr:
            cnt_prev = subseqs.get(n, 0)
            cnt_next = subseqs.get(n+difference,0)
            subseqs[n+difference] = max(cnt_prev + 1, cnt_next)
        
        return max(subseqs.values())

obj = Solution()
#data = obj.longestSubsequence(arr = [1,2,3,4], difference = 1)
#data = obj.longestSubsequence(arr = [1,3,5,7], difference = 1)
data = obj.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2)
print(data)