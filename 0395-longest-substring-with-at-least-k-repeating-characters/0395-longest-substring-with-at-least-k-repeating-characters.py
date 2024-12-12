class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        from collections import Counter
        freq = Counter(s)

        for c in freq:
            if freq[c] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))

        return len(s)
