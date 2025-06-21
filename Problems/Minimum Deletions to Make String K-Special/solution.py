import io
from typing import List
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def lbs(arr, x):
            l, r = -1, len(arr) - 1
            while l + 1 != r:
                m = (l + r) // 2
                if arr[m] < x:
                    l = m
                else:
                    r = m
            return r

        cntr = Counter(word)
        cntr = sorted(cntr.values())
        sums = reduce(lambda a, b: a + [a[-1] + b], cntr, [0])
        
        ans = float('inf')
        for i in range(len(cntr)):
            right_value = cntr[i] + k
            r = lbs(cntr, right_value)
            a = sums[i]
            if cntr[r] >= right_value: 
                a += sums[-1] - sums[r] - (right_value * (len(cntr) - r))
            if a < ans:
                ans = a
        return ans

obj = Solution()
#data = obj.minimumDeletions(word = "aabcaba", k = 0)
#data = obj.minimumDeletions(word = "dabdcbdcdcd", k = 2)
data = obj.minimumDeletions(word = "aaabaaa", k = 2)
print(data)