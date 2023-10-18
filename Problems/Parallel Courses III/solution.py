import io
from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=defaultdict(list)
        for required,course in relations:
            graph[course].append(required)

        @cache
        def dp (i):
            if not graph.get(i,False):
                return time[i-1]
            ans=-1
            for j in graph[i]:
                ans=max(ans,dp(j))
            return ans+time[i-1]
        return max([dp(i+1) for i in range(n)])

obj = Solution()
#data = obj.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])
data = obj.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])
print(data)