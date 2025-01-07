class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, word in enumerate(words):
            for j, target in enumerate(words):
                if i != j and word in target:
                    result.append(word)
                    break
        return result