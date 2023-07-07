import io
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        counter = {'T': 0, 'F': 0}
        left = 0
        right = 0
        max_length = 0
        max_count = 0

        while right < n:
            counter[answerKey[right]] += 1
            max_count = max(max_count, counter[answerKey[right]])
            length = right - left + 1
            if length - max_count > k:
                counter[answerKey[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
obj = Solution()
#data = obj.maxConsecutiveAnswers(answerKey = "TTFF", k = 2)
#data = obj.maxConsecutiveAnswers(answerKey = "TFFT", k = 1)
data = obj.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)
print(data)