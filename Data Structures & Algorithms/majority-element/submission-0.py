class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        hash_map= {}
        
        max_freq_num = nums[0]
        n = len(nums)
        max_freq = n//2
        for num in nums:
            hash_map[num] = hash_map.get(num ,0) +1
            if hash_map[num] >= max_freq:
                max_freq = max(max_freq, hash_map[num] )
                max_freq_num =num
        return max_freq_num

        