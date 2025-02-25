import io
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        odd_cnt, even_cnt = 0, 1
        curr_sum, res = 0, 0
        
        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                res += odd_cnt
                even_cnt += 1
            else:
                res += even_cnt
                odd_cnt += 1
                
        return res % mod

obj = Solution()
#data = obj.numOfSubarrays(arr = [1,3,5])
#data = obj.numOfSubarrays(arr = [2,4,6])
data = obj.numOfSubarrays(arr = [1,2,3,4,5,6,7])
print(data)