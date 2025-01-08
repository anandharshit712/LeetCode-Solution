class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    is_prefix = words[j][:len(words[i])] == words[i]
                    is_suffix = words[j][-len(words[i]):] == words[i]

                    if is_prefix and is_suffix:
                        count += 1
        return count