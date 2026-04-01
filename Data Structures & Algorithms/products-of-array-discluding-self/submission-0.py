class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *=  nums[i]
        print(res)
        suffix = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res