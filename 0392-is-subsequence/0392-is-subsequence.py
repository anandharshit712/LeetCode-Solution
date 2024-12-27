class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in s:
            index = t.find(char, index) + 1
            if index == 0:
                return False
        return True