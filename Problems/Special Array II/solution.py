import io
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        id = 0
        parityIds = [id]
        for a, b in itertools.pairwise(nums):
            if a % 2 == b % 2:
                id += 1
            parityIds.append(id)

        for _from, to in queries:
            ans.append(parityIds[_from] == parityIds[to])

        return ans

obj = Solution()
#data = obj.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]])
data = obj.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]])
print(data)