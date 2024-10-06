import io
from typing import List
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
    
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')

        s1si, s1ei = 0, len(s1) - 1
        s2si, s2ei = 0, len(s2) - 1

        # Increment start indices while matching
        while s1si <= s1ei and s2si <= s2ei and s1[s1si] == s2[s2si]:
            s1si += 1
            s2si += 1

        # Decrement end indices while matching
        while s1ei >= s1si and s2ei >= s2si and s1[s1ei] == s2[s2ei]:
            s1ei -= 1
            s2ei -= 1

obj = Solution()
#data = obj.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")
#data = obj.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")
data = obj.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating")
print(data)