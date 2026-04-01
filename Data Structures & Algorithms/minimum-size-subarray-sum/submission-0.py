class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        sum_win = 0
        LENGTH = float('inf')
        for r in range(len(nums)):
            sum_win += nums[r]
            while sum_win >= target:
                LENGTH = min(LENGTH, r-L+1)
                sum_win = sum_win - nums[L]
                L+=1
            
        return 0 if LENGTH ==  float('inf') else LENGTH    

