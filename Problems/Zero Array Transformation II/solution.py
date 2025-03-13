import io
from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q_len = len(queries)
        
        def canZero(k: int) -> bool:
            diff = [0] * (n + 1)
            
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            

            coverage = [0] * n
            coverage[0] = diff[0]
            for i in range(1, n):
                coverage[i] = coverage[i - 1] + diff[i]
            
            for i in range(n):
                if coverage[i] < nums[i]:
                    return False
            return True
        
        left, right = 0, q_len
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canZero(mid):
                answer = mid
                right = mid - 1 
            else:
                left = mid + 1  
        
        return answer

obj = Solution()
#data = obj.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])
data = obj.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]])
print(data)