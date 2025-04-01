import io
from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        for i, (p, b) in enumerate(reversed(questions)):
            j = i - b - 1
            if j >= 0:
                dp[i] = max(dp[i-1], dp[j] + p)
            else:
                dp[i] = max(dp[i-1], p)
        return dp[-1]

obj = Solution()
#data = obj.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]])
data = obj.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]])
print(data)