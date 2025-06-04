import io
from typing import List
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word

        W = len(word)
        max_length = W - numFriends + 1

        options = []
        for i in range(W):
            options.append(word[i : min(W, i + max_length)])

        options.sort()

        return options[-1]

obj = Solution()
#data = obj.answerString(word = "dbca", numFriends = 2)
data = obj.answerString(word = "gggg", numFriends = 4)
print(data)