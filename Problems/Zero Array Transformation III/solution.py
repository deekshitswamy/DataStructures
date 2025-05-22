import io
import heapq
from typing import List
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key = lambda x: x[0])
        preSum = [0] * (len(nums)+1)

        validQueries = []
        k = 0
        currentSum = 0
        userQueries = 0

        for i in range(len(nums)):
            while k < len(queries) and queries[k][0] <= i:
                heapq.heappush(validQueries, -queries[k][1])
                k+=1

            while currentSum + preSum[i] < nums[i]:
                if len(validQueries) == 0 or -validQueries[0] < i:
                    return -1
            
                right = heapq.heappop(validQueries)
                right = -right

                preSum[i] += 1
                preSum[right + 1] -= 1
                userQueries += 1

            currentSum += preSum[i]
        return len(queries) - userQueries

obj = Solution()
#data = obj.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]])
#data = obj.maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]])
data = obj.maxRemoval(nums = [1,2,3,4], queries = [[0,3]])
print(data)