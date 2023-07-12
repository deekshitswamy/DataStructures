import io
from typing import List
from itertools import combinations
from collections import Counter

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        l=len(requests)
        for i in range(l,0,-1):
            for j in combinations(requests,i):
                if Counter(x for x ,y in j)==Counter(y for x,y in j):
                    return i
        return 0            

obj = Solution()
#data = obj.maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]])
#data = obj.maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]])
data = obj.maximumRequests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]])
print(data)