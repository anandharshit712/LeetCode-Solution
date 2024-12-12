class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def count_unique_chars(s):
            return len(set(s))
        max_len = 0
        total_unique_chars = count_unique_chars(s)
        for current_unique in range(1, total_unique_chars + 1):
            start = 0
            end = 0
            freq = Counter()
            unique_count = 0
            k_count = 0
            while end < len(s):
                if unique_count <= current_unique:
                    char = s[end]
                    freq[char] += 1
                    if freq[char] == 1:
                        unique_count += 1
                    if freq[char] == k:
                        k_count += 1
                    end += 1
                while unique_count > current_unique:
                    char = s[start]
                    if freq[char] == k:
                        k_count -= 1
                    freq[char] -= 1
                    if freq[char] == 0:
                        unique_count -= 1
                    start += 1
                if unique_count == k_count:
                    max_len = max(max_len, end - start)
        return max_len