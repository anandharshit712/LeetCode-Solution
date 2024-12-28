class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0] * (n - k + 1)


        current_sum = sum(nums[:k])
        sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum


        left = [0] * len(sums)
        best_left = 0
        for i in range(len(sums)):
            if sums[i] > sums[best_left]:
                best_left = i
            left[i] = best_left


        right = [0] * len(sums)
        best_right = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best_right]:
                best_right = i
            right[i] = best_right


        max_sum = 0
        result = [-1, -1, -1]
        for middle in range(k, len(sums) - k):
            l = left[middle - k]
            r = right[middle + k]
            total = sums[l] + sums[middle] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, middle, r]

        return result