from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())
        first, last = {}, {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
    
        min_len = float('inf')
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                min_len = min(min_len, length)
    
        return min_len