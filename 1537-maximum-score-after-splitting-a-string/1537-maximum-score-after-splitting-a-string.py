class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        max_score = 0
        left_zeros = 0
        current_ones = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                current_ones += 1

            score = left_zeros + (total_ones - current_ones)
            max_score = max(max_score, score)

        return max_score        