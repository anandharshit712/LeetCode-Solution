class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        smaller_list = min(len(word1), len(word2))
        for i in range(smaller_list):
            result.append(word1[i])
            result.append(word2[i])
        
        if len(word1) > smaller_list:
            result.extend(word1[smaller_list:])
        else:
            result.extend(word2[smaller_list:])
        return "".join(result)