class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        streak =0
        for num in nums:
            if num == 1:
                streak += 1
            else:
                streak = 0
            best = max(best, streak)
        return best