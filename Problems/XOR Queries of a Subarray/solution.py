import io
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        ans = []

        # Fill the prefix XOR array
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        # Process each query
        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] ^ prefix[left - 1])

        return ans

obj = Solution()
#data = obj.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]])
data = obj.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]])
print(data)