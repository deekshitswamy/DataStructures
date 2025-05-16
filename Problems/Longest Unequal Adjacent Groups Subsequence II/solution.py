import io
from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if self.hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j
        
        max_len = max(dp)
        max_index = dp.index(max_len)
        
        subsequence_indices = []
        current = max_index
        while current != -1:
            subsequence_indices.append(current)
            current = prev[current]
        subsequence_indices.reverse()
        
        return [words[i] for i in subsequence_indices]
    
    def hamming_distance(self, s1: str, s2: str) -> int:
        distance = 0
        for a, b in zip(s1, s2):
            if a != b:
                distance += 1
        return distance

obj = Solution()
#data = obj.getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2])
data = obj.getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4])
print(data)