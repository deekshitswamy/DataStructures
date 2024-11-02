import io
from typing import List
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Step 1: Split the sentence into words
        words = sentence.split()
        
        # Step 2: Check adjacent pairs and the circular condition
        for i in range(len(words)):
            last_char = words[i][-1]
            first_char = words[(i + 1) % len(words)][0]
            if last_char != first_char:
                return False
        
        return True

obj = Solution()
#data = obj.isCircularSentence(sentence = "leetcode exercises sound delightful")
#data = obj.isCircularSentence(sentence = "eetcode")
data = obj.isCircularSentence(sentence = "Leetcode is cool")
print(data)