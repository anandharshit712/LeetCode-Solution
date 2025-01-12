from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_count = Counter(s)
        odd_count = sum(1 for freq in char_count.values() if freq % 2 != 0)
        if k > len(s):
            return False
        if odd_count > k:
            return False
    
        return True