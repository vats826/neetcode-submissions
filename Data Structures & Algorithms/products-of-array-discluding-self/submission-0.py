class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                all_prod *= num
        output= [1]*n
        for i in range(n):
            if zero_count == 0:
                output[i] = all_prod // nums[i]
            elif zero_count == 1:
                output[i] = all_prod if nums[i] == 0 else 0
            else:
                output[i] = 0
        return output