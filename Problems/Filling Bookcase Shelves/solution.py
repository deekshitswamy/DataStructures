import io
from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width = 0
            height = 0
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[n]

obj = Solution()
#data = obj.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4)
data = obj.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6)
print(data)