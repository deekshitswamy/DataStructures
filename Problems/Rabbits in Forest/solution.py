import io
from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        d = defaultdict(int)
        for i, a in enumerate(answers):
            d[a] += 1
        res = 0
        for k, v in d.items():
            if k == 0:
                res += v
                continue
            temp = k
            while k < v - 1:
                k += temp + 1
            res += k + 1
        return res

obj = Solution()
#data = obj.numRabbits(answers = [1,1,2])
data = obj.numRabbits(answers = [10,10,10])
print(data)