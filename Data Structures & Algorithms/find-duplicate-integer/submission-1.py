class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # 1 3 2 4 2    
        for num in nums:
            val = abs(num)
            if nums[val-1] < 0:
                return val
            nums[val-1] = nums[val-1] * -1
        return -1