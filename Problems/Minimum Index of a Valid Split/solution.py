import io
from typing import List
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        dom_term = 0
        for k, v in freq.items():
            if v > n / 2:
                dom_term = k
                break
        
        freq_dom_term = 0
        for i, num in enumerate(nums):
            if num == dom_term:
                freq_dom_term += 1

            if (i + 1) // 2 < freq_dom_term and (n - i - 1) // 2 < freq[dom_term] - freq_dom_term:
                return i
        
        return -1

obj = Solution()
#data = obj.minimumIndex(nums = [1,2,2,2])
#data = obj.minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1])
data = obj.minimumIndex(nums = [3,3,3,3,7,2,2])
print(data)