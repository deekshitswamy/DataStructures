import io
from typing import List
class Solution:
    def isPrefixAndSuffix(self, a: str, b: str) -> bool:
        n, m = len(a), len(b)
        if n > m:
            return False
        return a == b[:n] and a == b[-n:]
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans

obj = Solution()
#data = obj.countPrefixSuffixPairs(words = ["a","aba","ababa","aa"])
#data = obj.countPrefixSuffixPairs(words = ["pa","papa","ma","mama"])
data = obj.countPrefixSuffixPairs(words = ["abab","ab"])
print(data)