class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        smaller_list = min(len(word1), len(word2))
        for i in range(smaller_list):
            result += word1[i] + word2[i]
        
        if len(word1) > smaller_list:
            result += word1[smaller_list:]
        else:
            result += word2[smaller_list:]
        return "".join(result)