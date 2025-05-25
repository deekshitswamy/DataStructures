import io
from typing import List
from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        found = defaultdict(int)

        for word in words:
            reversed_word = word[1] + word[0]
            if found[reversed_word] >= 1:
                found[reversed_word] -= 1
                res += 4
            else:
                found[word] += 1

        for word, count in found.items():
            if count > 0 and word[0] == word[1]:
                return res + 2
        
        return res

obj = Solution()
#data = obj.longestPalindrome(words = ["lc","cl","gg"])
#data = obj.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"])
data = obj.longestPalindrome(words = ["cc","ll","xx"])
print(data)