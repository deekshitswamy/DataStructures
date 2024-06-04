import io
from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> int:
        residue_text = []
        len_palindrome = 0
        s = ''.join(sorted(s))
        print(s)
        for i in s:
            if i in residue_text:
                residue_text.pop()
            else:
                residue_text.append(i)
        str(residue_text)
        if len(residue_text):
            len_palindrome = len(s) - len(residue_text) + 1
        else:
            len_palindrome = len(s)
        return len_palindrome

obj = Solution()
#data = obj.longestPalindrome(s = "abccccdd")
data = obj.longestPalindrome(s = "a")
print(data)