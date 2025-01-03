class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0
        count = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update left sum
            right_sum = total_sum - left_sum  # Compute right sum
            if left_sum >= right_sum:
                count += 1

        return count