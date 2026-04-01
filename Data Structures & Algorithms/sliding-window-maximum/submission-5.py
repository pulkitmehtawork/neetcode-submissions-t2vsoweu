class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        output = []
        for i in range(n-k+1):
            max_num =nums[i]
            for j in range(i , i+k):
                max_num = max(max_num,nums[j])
            output.append(max_num)
        return output
            
            