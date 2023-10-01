import io
from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])

obj = Solution()
#data = obj.reverseWords(s = "Let's take LeetCode contest")
data = obj.reverseWords(s = "God Ding")
print(data)