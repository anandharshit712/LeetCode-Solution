class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zeros += 1

        if zeros > 1:
            return [0] * len(nums)
        
        result = []
        for num in nums:
            if zeros == 0:
                result.append(total_product // num)
            else:
                result.append(total_product if num == 0 else 0)
        
        return result