import io
from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        left_max = [0] * n
        right_max = [0] * n

        # Compute left_max array
        left_max[0] = values[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], values[i] + i)

        # Compute right_max array
        right_max[n - 1] = values[n - 1] - (n - 1)
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], values[i] - i)

        # Compute the maximum score
        maxi = 0
        for i in range(1, n):
            maxi = max(maxi, left_max[i - 1] + right_max[i])

        return maxi

obj = Solution()
#data = obj.maxScoreSightseeingPair(values = [8,1,5,2,6])
data = obj.maxScoreSightseeingPair(values = [1,2])
print(data)