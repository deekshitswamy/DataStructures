import io
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        N = 1
        while N < n:
            N *= 2
        tree = [0] * (2 * N)
        for i in range(n):
            tree[N + i] = baskets[i]
        for i in range(N - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])
        res = 0
        for fruit in fruits:
            if tree[1] < fruit:
                res += 1
                continue
            pos = 1
            while pos < N:
                if tree[2 * pos] >= fruit:
                    pos = 2 * pos
                else:
                    pos = 2 * pos + 1
            tree[pos] = 0
            pos //= 2
            while pos:
                tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
        return res

obj = Solution()
#data = obj.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
data = obj.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])
print(data)