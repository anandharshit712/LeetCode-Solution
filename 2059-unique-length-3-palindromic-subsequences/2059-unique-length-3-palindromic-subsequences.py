class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}

        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        unique_palindrome = set()

        for char in first_occurrence:
            start = first_occurrence[char]
            end = last_occurrence[char]
            if end - start > 1:
                middle_char = set(s[start + 1:end])
                for mid in middle_char:
                    unique_palindrome.add((char, mid, char))
        return len(unique_palindrome)