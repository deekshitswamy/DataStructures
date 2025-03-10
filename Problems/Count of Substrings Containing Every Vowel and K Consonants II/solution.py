import io
from typing import List
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        result = left = c = 0
        count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        vowels = "aeiou"

        ps = [len(word) for _ in range(len(word) + 1)]

        for i in range(len(word) - 1, -1, -1):
            if word[i] in vowels:
                ps[i] = ps[i + 1]
            else:
                ps[i] = i

        for right in range(len(word)):
            if word[right] in vowels:
                count[word[right]] += 1
            else:
                c += 1

            while c > k:
                if word[left] in vowels:
                    count[word[left]] -= 1
                else:
                    c -= 1

                left += 1

            while k == c and all(count[v] > 0 for v in vowels):
                result += ps[right + 1] - right

                if word[left] in vowels:
                    count[word[left]] -= 1
                else:
                    c -= 1
                
                left += 1
        
        return result

obj = Solution()
#data = obj.countOfSubstrings(word = "aeioqq", k = 1)
#data = obj.countOfSubstrings(word = "aeiou", k = 0)
data = obj.countOfSubstrings(word = "ieaouqqieaouqq", k = 1)
print(data)