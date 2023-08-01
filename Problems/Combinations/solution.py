import io
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1,curr = []):
            if len(curr) == k :
                output.append(curr[:])
                return 
            for i in range(first,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()
        output = []
        backtrack()
        return output

obj = Solution()
#data = obj.combine(n = 4, k = 2)
data = obj.combine(n = 1, k = 1)
print(data)