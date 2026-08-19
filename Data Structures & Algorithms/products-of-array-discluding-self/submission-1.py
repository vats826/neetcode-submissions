class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        prefix_prod = [1]*n
        suffix_prod = [1]*n
        for i in range(n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1] if i > 0 else 1
            suffix_prod[n-i-1] = suffix_prod[n-i]*nums[n-i] if i > 0 else 1
        for i in range(n):
            output[i] = prefix_prod[i] * suffix_prod[i]
        return output