import io
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = len(customers)
        min_penalty = penalty
        min_penalty_index = 0

        for i in range(1, len(customers)+1):
            if customers[i-1] == 'Y':
                penalty -= 1
            else:
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                min_penalty_index = i

        return min_penalty_index
obj = Solution()
#data = obj.bestClosingTime(customers = "YYNY")
#data = obj.bestClosingTime(customers = "NNNNN")
data = obj.bestClosingTime(customers = "YYYY")
print(data)