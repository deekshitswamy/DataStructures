import io
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set_words = set()
        dup_set = set()

        # Split sentences into words
        words1 = s1.split()
        words2 = s2.split()

        # Process words from the first sentence
        for word in words1:
            if word not in dup_set:
                if word in set_words:
                    set_words.remove(word)
                    dup_set.add(word)
                else:
                    set_words.add(word)

        # Process words from the second sentence
        for word in words2:
            if word not in dup_set:
                if word in set_words:
                    set_words.remove(word)
                    dup_set.add(word)
                else:
                    set_words.add(word)

        return list(set_words)

obj = Solution()
#data = obj.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour")
data = obj.uncommonFromSentences(s1 = "apple apple", s2 = "banana")
print(data)