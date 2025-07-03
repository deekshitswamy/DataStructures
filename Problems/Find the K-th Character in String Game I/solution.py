import io
from typing import List
class Solution:
    def kthCharacter(self, k: int) -> str:
        string="a"
        while len(string)<k:
            s1=""
            for i in range(len(string)):
                    s1+=str(chr(ord(string[i])+1))
            string+=s1
        return string[k-1]

obj = Solution()
#data = obj.kthCharacter(k = 5)
data = obj.kthCharacter(k = 10)
print(data)