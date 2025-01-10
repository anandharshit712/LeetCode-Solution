from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        frequency = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                frequency[char] = max(frequency[char], freq)
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= freq for char, freq in frequency.items()):
                result.append(word)
        return result
