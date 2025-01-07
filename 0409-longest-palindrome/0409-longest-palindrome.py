from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        palindorme_length = 0
        has_odd = False

        for count in count.values():
            if count % 2 == 0:
                palindorme_length += count
            else:
                palindorme_length += count - 1
                has_odd = True
            
        if has_odd:
            palindorme_length += 1
        return palindorme_length