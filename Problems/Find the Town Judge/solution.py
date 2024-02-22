import io
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_received = defaultdict(int)
        trusts_given = defaultdict(int)
        
        for t in trust:
            trusts_received[t[1]] += 1 
            trusts_given[t[0]] += 1    

        for person in range(1, n+1):
            if trusts_received[person] == n - 1 and trusts_given[person] == 0:
                return person
        return -1

obj = Solution()
#data = obj.findJudge(n = 2, trust = [[1,2]])
#data = obj.findJudge(n = 3, trust = [[1,3],[2,3]])
data = obj.findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])
print(data)