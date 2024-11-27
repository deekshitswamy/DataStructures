import io
from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dic = {end: [end-1] for end in range(1, n)} # add the original 1-step arrows
        res = []
        for j in range(len(queries)):
            dp = [0 if i == 0 else n for i in range(n)]
            dic[queries[j][1]].append(queries[j][0])
            # below, each query will be visited at most once so it's not really a "nested" loop
            for i in range(1, n):
                for start in dic[i]:
                    dp[i] = min(dp[i], dp[start]+1)
            res.append(dp[-1])
        return res


obj = Solution()
#data = obj.shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]])
data = obj.shortestDistanceAfterQueries(n = 4, queries = [[0,3],[0,2]])
print(data)